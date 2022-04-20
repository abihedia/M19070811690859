from odoo import models, fields, api

class PartnerHerit(models.Model):
    _inherit = 'res.partner'

    parc_machine = fields.One2many('fleet.vehicle', 'partner_id')
    num_siren = fields.Char('N° sirene')
    activity = fields.Char('activité')
    x_type_contact = fields.Selection([('societe', 'societe'), ('particulier', 'particulier')])
