from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta
#add field periodicité
class FleetContINHERIT(models.Model):
    _inherit = 'fleet.vehicle.log.contract'
    fleet_periodicite = fields.Selection([('mens', 'Mensuelle'), ('trim', 'Trimestrielle ')],string='Periodicité')
    fleet_date_inst   = fields.Date("Date d'installation")
    fleet_duree       = fields.Integer("Durée")
    fleet_duree_rest  = fields.Float("Durée restante",compute='duree_rest')
    fleet_prix_HT     = fields.Monetary("Prix HT")
    fleet_solde_est   = fields.Monetary("Solde estimatif",compute='solde_estimatif')

    @api.depends('fleet_prix_HT','fleet_duree_rest')
    def solde_estimatif(self):
        self.fleet_solde_est = self.fleet_prix_HT*self.fleet_duree_rest

    @api.depends('start_date')
    @api.onchange('start_date','fleet_duree','fleet_periodicite','expiration_date')
    def duree_rest(self):
        if self.expiration_date:
            if self.expiration_date >= date.today():
                nombre_jour=date.today()-self.start_date
                if self.fleet_periodicite == 'mens':
                    self.fleet_duree_rest = nombre_jour.days/30
                elif self.fleet_periodicite == 'trim':
                    self.fleet_duree_rest = nombre_jour.days/90
                else:
                    self.fleet_duree_rest =0
                    
            else:
                if self.fleet_periodicite == 'mens':
                    self.fleet_duree_rest = (self.expiration_date-self.start_date).days/30
                elif self.fleet_periodicite == 'trim':
                    self.fleet_duree_rest = (self.expiration_date-self.start_date).days/90
                else:
                    self.fleet_duree_rest =0
        else:
             self.fleet_duree_rest =0


    @api.onchange('start_date','fleet_duree','fleet_periodicite')
    def fleet_date_fin(self):
        if self.fleet_periodicite == 'mens':
            nombre_jour = self.fleet_duree * 30
            self.expiration_date = self.start_date + relativedelta(days=nombre_jour)
        if self.fleet_periodicite == 'trim':
            nombre_jour = self.fleet_duree * 90
            self.expiration_date = self.start_date + relativedelta(days=nombre_jour)

class FleetVehicleINHERIT(models.Model):
    _inherit = 'fleet.vehicle'
    comp_couleur = fields.Integer(string="Copies couleur", default=1)
    comp_noir = fields.Integer(string="Copies noir", default=1)

    def return_comp_coleur(self):
        pass
    def return_comp_noir(self):
        pass


















