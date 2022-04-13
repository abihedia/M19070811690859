from odoo import models, fields, api

class SaleOrderHerit(models.Model):
    _inherit = 'sale.order'
    sale_marge      = fields.Float(compute="sale_marge_fuc",default=0.0, string="Marge")

    def sale_marge_fuc(self):
        self.sale_marge = 0


