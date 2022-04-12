from odoo import models, fields, api

class CrmHerit(models.Model):
    _inherit = 'crm.lead'

    action_field = fields.Selection([('nouveau_client', 'Un nouveau client'), ('additionnel', 'Additionnel'),
                                               ('conversion', 'Conversion')])
    materiels = fields.Char('Matériels')
    num_dossier = fields.Char('Numéro de dossier', readonly=True)

    @api.model
    def create(self, vals):
        record = super(CrmHerit, self).create(vals)
        record['num_dossier'] = self.env['ir.sequence'].next_by_code('crm.num')
        return record



