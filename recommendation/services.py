from itertools import permutations

from boxes.models import Box


def can_fit_with_rotation(product, box):
    orientations = set(
        permutations(
            (
                product.length,
                product.width,
                product.height,
            )
        )
    )

    for length, width, height in orientations:

        if (
            box.length >= length and
            box.width >= width and
            box.height >= height
        ):
            return True

    return False


def get_best_box(product):

    suitable_boxes = []

    for box in Box.objects.all():

        dimensions_fit = can_fit_with_rotation(product,box)
        weight_supported = (box.max_weight >= product.weight)

        if dimensions_fit and weight_supported:
            wasted_space = (box.volume() -product.volume())
            suitable_boxes.append((box,wasted_space))

    if not suitable_boxes:
        return None

    suitable_boxes.sort(
        key=lambda item: (
            item[0].cost,
            item[1]
        )
    )
    return suitable_boxes[0][0]