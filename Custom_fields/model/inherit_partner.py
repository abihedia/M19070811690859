from odoo import models, fields, api

class ContactHerit(models.Model):
    _inherit = 'res.partner'

    siren_number = fields.Char('N° sirene')
    activity_partner = fields.Char('Activité')