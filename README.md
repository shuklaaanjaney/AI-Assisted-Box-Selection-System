# AI-Assisted Box Selection System

## Overview

This project is a Django REST Framework based application developed for an e-commerce warehouse scenario.

When a customer places an order, the warehouse team needs to determine which shipping box should be used. The recommendation process considers:

* Product dimensions
* Product weight
* Box dimensions
* Box weight capacity
* Box cost

The system recommends the most suitable box while ensuring that the product can fit safely within the box and that the box can support the product's weight.

---

## Business Objective

The primary objective is to recommend a shipping box that satisfies operational constraints while minimizing shipping cost.

The recommendation strategy prioritizes:

1. Dimension compatibility
2. Weight compatibility
3. Lowest box cost
4. Least unused space when costs are equal

This approach helps avoid selecting oversized boxes while still keeping packaging costs low.

---

## Features

* Product Management API
* Box Management API
* Order Management API
* Box Recommendation API
* Django Admin Support
* Automated Test Cases
* REST APIs built using Django REST Framework

---

## Technology Stack

* Python 3
* Django
* Django REST Framework (DRF)
* SQLite3

---

## Project Structure

```text
boxes/
recommendation/
config/

manage.py
requirements.txt
README.md
AI_USAGE.md
TEST_OUTPUT.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd AI-Assisted-Box-Selection-System
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

---

## API Endpoints

### Products

```http
GET /api/products/
POST /api/products/
```

### Boxes

```http
GET /api/boxes/
POST /api/boxes/
```

### Orders

```http
GET /api/orders/
POST /api/orders/
```

### Recommendation

```http
GET /api/recommendation/<product_id>/
```

Example:

```http
GET /api/recommendation/1/
```

Sample Response:

```json
{
    "product": "Laptop",
    "recommended_box": "Small Box",
    "cost": 50.0
}
```

---

## Recommendation Logic

The recommendation process follows these steps:

1. Retrieve the product details.
2. Identify boxes that can accommodate the product dimensions.
3. Verify that the box can support the product weight.
4. Calculate unused space for each valid box.
5. Select the lowest-cost valid box.
6. If multiple boxes have the same cost, select the box with the least unused space.

If no suitable box is found, the system returns no recommendation.

---

## Assumptions

* One product is evaluated at a time.
* Product dimensions and weight are expected to be valid values.
* Box dimensions represent usable internal dimensions.
* A valid recommendation must satisfy both dimension and weight requirements.
* Cost is prioritized over unused space.

---

## Edge Cases Considered

* Product does not fit in any available box.
* Product exceeds the weight capacity of available boxes.
* Multiple boxes satisfy the requirements.
* Multiple boxes have different costs.
* Multiple boxes have the same cost but different amounts of unused space.

---

## Current Limitations

The current implementation focuses on the assignment requirements and does not include:

* Product rotation/orientation optimization.
* Packing multiple products into a single box.
* Quantity-based packing calculations.
* Advanced bin-packing or warehouse optimization algorithms.

These can be considered future enhancements depending on business requirements.

---

## Running Tests

Run all tests using:

```bash
python manage.py test
```

Current test coverage includes:

* Product creation validation
* Recommendation service validation
* No suitable box scenario
* Lowest-cost box selection
* Recommendation API endpoint testing

Test execution output is available in:

```text
TEST_OUTPUT.md
```

---

## Additional Documentation

The repository also contains:

* README.md
* AI_USAGE.md
* TEST_OUTPUT.md

---

## Author

Aanjaney Shukla
