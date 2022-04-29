from odoo import models, fields, api
from datetime import date
import math
from dateutil.relativedelta import relativedelta
#add field periodicité
class FleetContINHERIT(models.Model):
    _inherit = 'fleet.vehicle'
    fleet_type_materiel=  fields.Char(string="Type de matériel")
    image_materiel  = fields.Binary()
    model_id = fields.Many2one(required=False )


    ##############
    #   Contrat  #
    #############
    fleet_periodicite = fields.Selection([('mens', 'Mensuelle'), ('trim', 'Trimestrielle ')],string='Periodicité')
    fleet_date_inst   = fields.Date("Date d'installation")
    fleet_expiration_date = fields.Date("Date de fin de contrat")
    fleet_duree       = fields.Integer("Durée de contrat")
    fleet_duree_rest  = fields.Integer("Durée restante",compute='duree_rest')
    fleet_prix_HT     = fields.Monetary("Prix HT")
    fleet_solde_est   = fields.Monetary("Solde estimatif",compute='solde_estimatif')
    fleet_type = fields.Char(string="Type de vente", default='Location')
    fleet_leaser = fields.Char(string="Leaser")
    fleet_accord = fields.Char(string="N° d'accord")

    fleet_trimestre_help = fields.Char(string="help ", compute="trimestre_help")
    fleet_trimestre_help1 = fields.Char(string="help 1", compute="trimestre_help1")

    @api.depends('fleet_periodicite','fleet_duree')
    def trimestre_help(self):
        for rec in self:
            if rec.fleet_periodicite =='trim':
                if rec.fleet_duree > 1:
                    rec.fleet_trimestre_help = "Trimestres"
                else:
                    rec.fleet_trimestre_help = "Trimestre"
            elif rec.fleet_periodicite =='mens':
                rec.fleet_trimestre_help = "Mois"
            else:
                rec.fleet_trimestre_help = " "
    @api.depends('fleet_periodicite','fleet_duree_rest')
    def trimestre_help1(self):
        for rec in self:
            if rec.fleet_periodicite =='trim':
                if rec.fleet_duree_rest > 1:
                    rec.fleet_trimestre_help1 = "Trimestres"
                else:
                    rec.fleet_trimestre_help1 = "Trimestre"

            elif rec.fleet_periodicite =='mens':
                rec.fleet_trimestre_help1 = "Mois"
            else:
                rec.fleet_trimestre_help1 = " "

    @api.depends('fleet_prix_HT','fleet_duree_rest')
    def solde_estimatif(self):
        for rec in self:
            rec.fleet_solde_est = self.fleet_prix_HT*self.fleet_duree_rest

    @api.depends('fleet_expiration_date')
    @api.onchange('fleet_date_inst', 'fleet_duree', 'fleet_periodicite', 'fleet_expiration_date')
    def duree_rest(self):
        for rec in self:
            if rec.fleet_expiration_date:
                if rec.fleet_expiration_date > date.today():
                    if rec.fleet_periodicite == 'mens':
                        date1 = date.today()-relativedelta(days=1)
                        date2 = rec.fleet_expiration_date
                        num_months = (date2.year - date1.year) * 12 + (date2.month - date1.month)
                        if num_months>1:
                            rec.fleet_duree_rest = num_months-1
                        else:
                            rec.fleet_duree_rest = 0
                    elif rec.fleet_periodicite == 'trim':
                        date1 = date.today() - relativedelta(days=1)
                        date2 = rec.fleet_expiration_date
                        num_months = (date2.year - date1.year) * 12 + (date2.month - date1.month)
                        rec.fleet_duree_rest = math.floor(num_months/3)
                    else:
                        rec.fleet_duree_rest = 0
                else:
                    rec.fleet_duree_rest = 0
            else:
                rec.fleet_duree_rest = 0
    @api.onchange('fleet_date_inst','fleet_duree','fleet_periodicite')
    def fleet_date_fin(self):
        for rec in self:
            if rec.fleet_date_inst:
                if rec.fleet_periodicite == 'mens':
                    if rec.fleet_duree>0:
                        rec.fleet_expiration_date = rec.fleet_date_inst + relativedelta(months=rec.fleet_duree)-relativedelta(days=1)
                    else:
                        rec.fleet_expiration_date = rec.fleet_date_inst

                if rec.fleet_periodicite == 'trim':
                    if rec.fleet_duree>0:
                        rec.fleet_expiration_date = rec.fleet_date_inst + relativedelta(months=(rec.fleet_duree*3)) - relativedelta(days=1)
                    else:
                        rec.fleet_expiration_date = rec.fleet_date_inst


    ####################
    #  infos MATÉRIELS #
    ####################
    partner_id = fields.Many2one('res.partner', ondelete='Set null', string='Client', index=True)
    fleet_serie = fields.Char(string="N° serie")
    fleet_fournisseur = fields.Many2one('res.partner', ondelete='Set null',string="Fournisseur",index=True)
    fleet_marque = fields.Many2one( "fleet.vehicle.model",string='Marque')
    fleet_Modele = fields.Char(string="Modèle")
    fleet_equipement = fields.Char(string="Équipement")
    fleet_type_1 = fields.Char(string="Type")
    fleet_installation = fields.Char(string="Lieu d'installation")
    fleet_commentaires = fields.Text(string="Commentaires")

    ######################
    #  infos MAINTENANCE #
    ###################### Mensuelle
    fleet_facturation = fields.Selection([('mens', 'MENSUELLE'), ('trim', 'TRIMESTRIELLE')], string='Facturation')
    @api.onchange('fleet_periodicite')
    def facturationType(self):
        for rec in self:
            if rec.fleet_periodicite == 'trim':
                rec.fleet_facturation = 'trim'
            if rec.fleet_periodicite == 'mens':
                rec.fleet_facturation = 'mens'

    fleet_cout_Couleur = fields.Monetary(string="Cout copie COULEUR")
    fleet_forfait_couleur = fields.Integer(string="Forfait COULEUR")
    fleet_cout_nb = fields.Monetary(string="Cout copie NB")
    fleet_forfait_nb = fields.Integer(string="Forfait NB")
    fleet_abonnement_service = fields.Monetary(string="Abonnement Service")
    fleet_autre = fields.Monetary(string="Autre")
                             ############# help Unit
    fleet_unit_HT_Copie = fields.Char(string="help 1", compute="HT_Copie")
    def HT_Copie(self):
        for rec in self:
            rec.fleet_unit_HT_Copie="HT/Copie"
    fleet_unit_Copie = fields.Char(string="help 1", compute="Copie_unit")
    def Copie_unit(self):
        for rec in self:
            rec.fleet_unit_Copie ="Copies"

    ######################
    #  infos FINANCIERES #
    ######################
    fleet_partenariat = fields.Monetary(string="Partenariat")
    fleet_date_fin_F = fields.Date("Date de fin")
    fleet_solde_fois = fields.Monetary(string="Solde en 2 fois(1er solde)")
    fleet_date_2_solde = fields.Date("Date de 2éme solde à faire")
    fleet_solde_Montant = fields.Monetary(string="Montant de 2éme solde")




   ############
    #  Vehicle #
    ############
    comp_couleur = fields.Integer(string="Compteur Couleur", default=1)
    comp_noir = fields.Integer(string="Compteur NB", default=1)


    def return_comp_coleur(self):
        pass

    def return_comp_noir(self):
        pass





















