from odoo import models, fields, api
from odoo.exceptions import ValidationError


class InventoryStockOut(models.Model):
    _name = "inventory.stock.out"
    _description = "Inventory Stock Out"

    name = fields.Char(
        string="Reference",
        default="New",
        readonly=True,
        copy=False
    )

    date = fields.Date(
        string="Date",
        default=fields.Date.today
    )

    product_id = fields.Many2one(
        "inventory.product",
        string="Product",
        required=True
    )

    qty = fields.Integer(
        string="Quantity",
        required=True
    )

    description = fields.Text(
        string="Description"
    )

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)

        for record in records:

            if record.product_id.stock < record.qty:
                raise ValidationError("Stock tidak mencukupi.")

            if record.name == "New":
                record.name = self.env["ir.sequence"].next_by_code(
                    "inventory.stock.out"
                ) or "New"

            if record.qty > record.product_id.stock:
                raise ValidationError("Stock tidak mencukupi.")
                
            record.product_id.stock -= record.qty

        return records