from odoo import models, fields


class InventoryCategory(models.Model):
    _name = "inventory.category"
    _description = "Inventory Category"

    name = fields.Char(
        string="Category Name",
        required=True
    )

    description = fields.Text(
        string="Description"
    )

    active = fields.Boolean(
        default=True
    )