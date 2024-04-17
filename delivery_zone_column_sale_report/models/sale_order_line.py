from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.report'

    delivery_zone_id = fields.Many2one(
        comodel_name="partner.delivery.zone",
        string="Delivery Zone",
        readonly=True,
    )

    def _select_additional_fields(self, fields):
        fields['delivery_zone_id'] = ", s.delivery_zone_id as delivery_zone_id"
        return super()._select_additional_fields(fields)
