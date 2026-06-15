# AI-Assisted Box Selection System

## Overview

This project is a Django-based box recommendation system developed for an e-commerce warehouse scenario.
When a customer places an order, the system recommends the most suitable shipping box based on:

* Product dimensions
* Product weight
* Box dimensions
* Box weight capacity
* Box cost

The recommendation algorithm selects the lowest-cost box that can safely accommodate the product. If multiple boxes have the same cost, the box with the least unused space is preferred.

---

## Features

* Product Management API
* Box Management API
* Order Management API
* Box Recommendation API
* Django Admin Panel
* Automated Test Cases
* RESTful APIs using Django REST Framework

---

## Tech Stack

* Python 3
* Django
* Django REST Framework (DRF)

---

## Project Structure

```text
boxes/
recommendation/
config/
manage.py
db.sqlite3
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd tradexa_box_selector
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

Run the server:

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

Response:

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

1. Identify boxes that can fit the product dimensions.
2. Verify that the box supports the product weight.
3. Select the lowest-cost valid box.
4. If multiple boxes have the same cost, choose the box with the least unused space.

---

## Running Tests

Run all tests:

```bash
python manage.py test
```

Current test coverage includes:

* Product creation validation
* Recommendation service validation
* No suitable box scenario
* Cheapest box selection
* Recommendation API endpoint testing

---

## Author

Aanjaney Shukla
