from boxes.models import Box


def get_best_box(product):

    suitable_boxes = []

    for box in Box.objects.all():

        dimensions_fit = (
            box.length >= product.length and
            box.width >= product.width and
            box.height >= product.height
        )

        weight_supported = (box.max_weight >= product.weight)

        if dimensions_fit and weight_supported:
            wasted_space = box.volume() - product.volume()
            suitable_boxes.append((box, wasted_space))

    if not suitable_boxes:
        return None

    suitable_boxes.sort(key=lambda item: (item[0].cost,item[1]))

    return suitable_boxes[0][0]