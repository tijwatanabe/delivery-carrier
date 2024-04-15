from odoo import fields, models, tools

class SaleOrderLine(models.Model):
    _inherit = 'sale.report'

    delivery_zone_id = fields.Char('Delivery Zone')

    def _select_additional_fields(self, fields):
        fields['delivery_zone_id'] = ", s.delivery_zone_id as delivery_zone_id"
        return super()._select_additional_fields(fields)
