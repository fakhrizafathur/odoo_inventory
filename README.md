# Inventory Management System - Odoo 19

A simple Inventory Management module developed using **Odoo 19**. This module was created as a learning project to understand custom module development in Odoo, including models, views, menus, and stock management.

## Features

- Category Management
- Product Management
- Stock In Transaction
- Stock Out Transaction
- Automatic Stock Update
- Inventory Report
- Simple Dashboard Menu

## Technologies

- Odoo 19
- Python
- PostgreSQL
- XML
- ORM (Odoo Framework)

## Module Structure

```
inventory_management/
│
├── models/
│   ├── category.py
│   ├── product.py
│   ├── stock_in.py
│   ├── stock_out.py
│   └── __init__.py
│
├── security/
│   └── ir.model.access.csv
│
├── views/
│   ├── menu.xml
│   ├── category_views.xml
│   ├── product_views.xml
│   ├── stock_in_views.xml
│   ├── stock_out_views.xml
│   └── report_views.xml
│
├── demo/
│
├── __manifest__.py
└── __init__.py
```

## Database Models

### Inventory Category

| Field       | Type    |
| ----------- | ------- |
| Name        | Char    |
| Description | Text    |
| Active      | Boolean |

---

### Inventory Product

| Field    | Type     |
| -------- | -------- |
| Name     | Char     |
| Category | Many2one |
| Stock    | Integer  |
| Price    | Float    |
| Active   | Boolean  |

---

### Stock In

| Field    | Type     |
| -------- | -------- |
| Product  | Many2one |
| Quantity | Integer  |
| Date     | Date     |
| Notes    | Text     |

---

### Stock Out

| Field    | Type     |
| -------- | -------- |
| Product  | Many2one |
| Quantity | Integer  |
| Date     | Date     |
| Notes    | Text     |

## How It Works

### Stock In

When a Stock In transaction is created:

- Select Product
- Input Quantity
- Save Transaction
- Product Stock will automatically increase

### Stock Out

When a Stock Out transaction is created:

- Select Product
- Input Quantity
- Save Transaction
- Product Stock will automatically decrease

## Installation

1. Copy the module into the `custom_addons` directory.

```
custom_addons/
    inventory_management/
```

2. Add the custom addons path inside `odoo.conf`.

```ini
addons_path = D:\odoo19\odoo\addons,D:\odoo19\custom_addons
```

3. Restart Odoo.

4. Activate **Developer Mode**.

5. Click **Apps → Update Apps List**.

6. Search for **Inventory Management**.

7. Click **Install**.

## Future Improvements

- Supplier Management
- Customer Management
- Purchase Transaction
- Sales Transaction
- Stock History
- Barcode Support
- Dashboard with Charts
- PDF Report
- Excel Export
- User Role & Access Control

## Author

**Fathur Fakhriza**

- GitHub: https://github.com/fakhrizafathur
- LinkedIn: https://www.linkedin.com/in/fathur-fakhriza-8b6941215/
