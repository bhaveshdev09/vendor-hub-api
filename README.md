# Vendor Hub API

A Vendor Management System(VMS) apis  for efficient vendor profile management, purchase order tracking, and vendor performance metrics calculation.

![Python version](https://img.shields.io/badge/Python-3.10.8-4c566a?logo=python&&longCache=true&logoColor=white&colorB=pink&style=flat-square&colorA=4c566a) ![Django version](https://img.shields.io/badge/Django-4.2.8-4c566a?logo=django&&longCache=truelogoColor=white&colorB=pink&style=flat-square&colorA=4c566a) ![Django-RestFramework version](https://img.shields.io/badge/Django_Rest_Framework-3.14.0-red.svg?longCache=true&style=flat-square&logo=django&logoColor=white&colorA=4c566a&colorB=pink)  ![Last Commit](https://img.shields.io/github/last-commit/bhaveshdev09/vendor-hub-api/master?&&longCache=true&logoColor=white&colorB=green&style=flat-square&colorA=4c566a) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

- [Core Features](#features)
- [Project Plan](#planning)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Core Features

1. **Vendor Profile Management:**

   - Create, retrieve, update, and delete vendor profiles.
   - Track vendor information including name, contact details, address, and a unique vendor code.
2. **Purchase Order Tracking:**

   - Create, retrieve, update, and delete purchase orders.
   - Track purchase order details such as PO number, vendor reference, order date, items, quantity, and status.
3. **Vendor Performance Evaluation:**

   - Calculate vendor performance metrics, including on-time delivery rate, quality rating average, average response time, and fulfillment rate.
   - Retrieve performance metrics for a specific vendor.

## Project Plan 

To access the project plan, please visit the following URL: [Vendor Hub API](https://github.com/users/bhaveshdev09/projects/1)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/vendor-management-system.git
   cd vendor-management-system
   ```
2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Apply database migrations:

   ```bash
   python manage.py migrate
   ```
4. Run the development server:

   ```bash
   python manage.py runserver
   ```
5. Access the application at http://localhost:8000.

## API Endpoints

Below is a summary of the available API endpoints:

**Vendor Profile Management**

| Endpoint               | Method      | Description                           |
| ---------------------- | ----------- | ------------------------------------- |
| `/api/vendors/`      | POST        | Create a new vendor.                  |
| `/api/vendors/`      | GET         | List all vendors.                     |
| `/api/vendors/{id}/` | GET         | Retrieve a specific vendor's details. |
| `/api/vendors/{id}/` | PUT / PATCH | Update a vendor's details.            |
| `/api/vendors/{id}/` | DELETE      | Delete a vendor.                      |

**Purchase Order Tracking**

| Endpoint                                  | Method       | Description                                    |
| ----------------------------------------- | ------------ | ---------------------------------------------- |
| `/api/purchase_orders/`                 | POST         | Create a purchase order.                       |
| `/api/purchase_orders/`                 | GET          | List all purchase orders.                      |
| `/api/purchase_orders/{id}/`            | GET          | Retrieve details of a specific purchase order. |
| `/api/purchase_orders/{id}/`            | PUT / PATCH  | Update a purchase order.                       |
| `/api/purchase_orders/{id}/`            | DELETE       | Delete a purchase order.                       |
| `/api/purchase_orders/{id}/acknowledge` | PUT / PATCH | Acknowledge a purchase order.                  |

**Vendor Performance Evaluation**

| Endpoint                                  | Method | Description                              |
| ----------------------------------------- | ------ | ---------------------------------------- |
| `/api/vendors/{id}/performance`         | GET    | Retrieve a vendor's performance metrics. |
| `/api/vendors/{id}/performance/history` | GET    | Retrieve a vendor's performance history. |

**Additional Docs**

| Endpoint                                      | Method | Description                                                   |
| --------------------------------------------- | ------ | ------------------------------------------------------------- |
| `/api/vendors/{id}/performance/schema/doc/` | GET    | List all the apis in Open API3 documentation format.          |
| `/api/vendors/{id}/performance/schema/doc/` | GET    | List all the apis in Open API3 detailed documentation format. |

## Testing

Run the tests using the following command:

```bash
python manage.py test
```

To check coverage report of the entire codebases try this command:

```bash
coverage run manage.py test

# to get the coverage report on command line
coverage report -m

# To get the html report of code coverage try this
coverage html
```

## Contributing

Inputs and contributions to this project are appreciated. To make them as transparent and easy as possible, please follow this steps:

- ### How to contribute:


  1. Fork the repository and create your branch from master with different name.
  2. Clone the project to your own machine
  3. Commit changes to your own branch
  4. Push your work back up to your fork
  5. Submit a Pull request

  ### Don't:

  - Don't include any license information when submitting your code as this repository is MIT licensed, and so your submissions are understood to be under the same MIT License as well.
- ### How to report a bug:


  1. Open a new Issue.
  2. Write a bug report with details, background, and when possible sample code. That's it!

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
