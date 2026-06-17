# AI-Assisted Box Selection System

## Overview

This project is a Django REST Framework (DRF) based box recommendation system designed for an e-commerce warehouse scenario.

When a customer places an order, the system recommends the most suitable shipping box by evaluating:

* Product dimensions
* Product weight
* Box dimensions
* Box weight capacity
* Box cost

The objective is to select a box that can safely accommodate the product while minimizing packaging cost and reducing wasted space.

---

## Business Objective

Warehouses often maintain multiple box sizes with different costs and capacities. Selecting an unsuitable box can increase shipping expenses, waste packaging material, or fail to protect the product during transit.

This system automates box selection using the following priority:

1. Dimension compatibility
2. Weight compatibility
3. Lowest box cost
4. Least unused space when costs are equal

---

## Features

* Product Management API
* Box Management API
* Order Management API
* Box Recommendation API
* Django Admin Integration
* Automated Unit Tests
* Product Rotation Support
* Weight Capacity Validation
* Model-Level Data Validation
* RESTful APIs using Django REST Framework

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

Move to the project directory:

```bash
cd AI-Assisted-Box-Selection-System
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

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

## Recommendation Algorithm

The recommendation process follows these steps:

1. Retrieve the selected product.
2. Check whether the product can fit inside each available box.
3. Evaluate all possible product orientations (rotation support).
4. Verify that the box weight capacity can support the product.
5. Calculate unused space for every valid box.
6. Select the lowest-cost valid box.
7. If multiple boxes have the same cost, choose the box with the least unused space.

If no suitable box exists, the system returns no recommendation.

---

## Validation Rules

### Product Validation

The system prevents:

* Negative length values
* Negative width values
* Negative height values
* Negative weight values

### Box Validation

The system prevents:

* Negative dimensions
* Negative weight capacity
* Negative box cost

---

## Assumptions

* One product is evaluated at a time.
* Product dimensions represent actual package dimensions.
* Box dimensions represent usable internal dimensions.
* Products may be rotated to fit inside a box.
* A valid recommendation must satisfy both dimension and weight requirements.
* Cost is prioritized over unused space.

---

## Edge Cases Covered

* Product does not fit inside any available box.
* Product exceeds the weight capacity of all boxes.
* Product only fits after rotation.
* Multiple boxes satisfy the requirements.
* Multiple boxes have different costs.
* Multiple boxes have identical costs but different unused space values.
* Invalid negative product dimensions.
* Invalid negative box dimensions.

---

## Current Limitations

The current implementation focuses on the assignment requirements and does not include:

* Multiple products per order
* Quantity-based packing calculations
* Warehouse packing optimization
* Advanced 3D bin-packing algorithms

These can be considered future enhancements depending on business requirements.

---

## Testing

Run all tests:

```bash
python manage.py test
```

Current automated test coverage includes:

* Product creation validation
* Box recommendation validation
* Cheapest box selection
* No suitable box scenario
* Product rotation handling
* Weight capacity validation
* Product model validation
* Box model validation
* Recommendation API endpoint testing

### Current Test Results

```text
Ran 9 tests

OK
```

Full test execution output is available in:

```text
TEST_OUTPUT.md
```

---

## Additional Documentation

The repository contains:

* README.md
* AI_USAGE.md
* TEST_OUTPUT.md

---

## Author

Aanjaney Shukla
