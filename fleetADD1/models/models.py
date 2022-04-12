from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta
#add field periodicité
class FleetContINHERIT(models.Model):
    _inherit = 'fleet.vehicle'

    ##############
    #   Contrat  #
    #############
    fleet_periodicite = fields.Selection([('mens', 'Mensuelle'), ('trim', 'Trimestrielle ')],string='Periodicité')
    fleet_date_inst   = fields.Date("Date d'installation")
    fleet_expiration_date = fields.Date("Date de fin de contrat")
    fleet_duree       = fields.Integer("Durée de contrat")
    fleet_duree_rest  = fields.Float("Durée restante",compute='duree_rest')
    fleet_prix_HT     = fields.Monetary("Prix HT")
    fleet_solde_est   = fields.Monetary("Solde estimatif",compute='solde_estimatif')
    @api.depends('fleet_prix_HT','fleet_duree_rest')
    def solde_estimatif(self):
        self.fleet_solde_est = self.fleet_prix_HT*self.fleet_duree_rest

    @api.depends('fleet_expiration_date')
    @api.onchange('fleet_date_inst', 'fleet_duree', 'fleet_periodicite', 'fleet_expiration_date')
    def duree_rest(self):
        if self.fleet_expiration_date:
            if self.fleet_expiration_date > date.today():
                if self.fleet_periodicite == 'mens':
                    self.fleet_duree_rest = round((self.fleet_expiration_date - date.today()).days / 30)
                elif self.fleet_periodicite == 'trim':
                    self.fleet_duree_rest = round((self.fleet_expiration_date - date.today()).days / 90)
                else:
                    self.fleet_duree_rest = 0
            else:
                self.fleet_duree_rest = 0
        else:
            self.fleet_duree_rest = 0            




    @api.onchange('fleet_date_inst','fleet_duree','fleet_periodicite')
    def fleet_date_fin(self):
        if self.fleet_date_inst:
            if self.fleet_periodicite == 'mens':
                nombre_jour = self.fleet_duree * 30
                self.fleet_expiration_date = self.fleet_date_inst + relativedelta(days=nombre_jour)
            if self.fleet_periodicite == 'trim':
                nombre_jour = self.fleet_duree * 90
                self.fleet_expiration_date = self.fleet_date_inst + relativedelta(days=nombre_jour)
    ############
    #  Vehicle #
    ############
    comp_couleur = fields.Integer(string="Copies couleur", default=1)
    comp_noir = fields.Integer(string="Copies noir", default=1)

    def return_comp_coleur(self):
        pass

    def return_comp_noir(self):
        pass





















