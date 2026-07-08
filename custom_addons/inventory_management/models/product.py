from odoo import models, fields


class InventoryProduct(models.Model):
    _name = "inventory.product"
    _description = "Inventory Product"

    name = fields.Char(
        string="Product Name",
        required=True
    )

    category_id = fields.Many2one(
        "inventory.category",
        string="Category",
        required=True
    )

    stock = fields.Integer(
        string="Stock",
        default=0
    )

    price = fields.Float(
        string="Price"
    )

    active = fields.Boolean(
        default=True
    )