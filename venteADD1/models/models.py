from odoo import models, fields, api

class SaleOrderHerit(models.Model):
    _inherit    = 'sale.order'
    sale_marge  = fields.Float(compute="sale_marge_fuc",default=0.0, string="Marge")

    #########  Financement page
    #group 1
    sale_type    = fields.Char(string="Type",default='Location')
    sale_leaser  = fields.Char(string="Leaser")
    sale_finance = fields.Monetary(string="Montant financé")
    #group 2
    sale_duree   = fields.Integer(string="Durée")
    sale_accord  = fields.Char(string="N° d'accord")
    sale_loyer   = fields.Monetary(string="Loyer")
    #group 3
    sale_periodicite = fields.Selection([('mens', 'Mensuelle'), ('trim', 'Trimestrielle ')], string='Periodicité')
    sale_reglement   = fields.Selection([('mens', 'Mensuelle'), ('trim', 'Trimestrielle ')], string='Mode de reglement')
    sale_frais       = fields.Monetary(string="Frais de livraison")
    #########  Rachats page
    #group 1
    sale_vr_client      = fields.Monetary(string="VR clients")
    sale_ir_prospects   = fields.Monetary(string="IR prospects")
    sale_rachat_matriel = fields.Monetary(string="Rachat matriél")
    #groupe 2
    sale_leaser_ra = fields.Char(string="Leaser")
    sale_partenariat = fields.Monetary(string="Partenariat")
    sale_marque_reference = fields.Char(string="Marque & référence")
    #groupe 3
    sale_accord_rachat = fields.Char(string="N° d'accord")
    sale_solde_2_fois = fields.Monetary(string="Solde en 2 fois")
    sale_Gratuite = fields.Monetary(string="Gratuitée")

    #########  Maintenance page
    # group 1
    sale_cout_signe_nb = fields.Monetary(string="Cout copie Signé ")
    sale_cout_actuel_nb = fields.Monetary(string="Cout copie Actuel ")
    sale_cout_actuel_signe_nb = fields.Monetary(string="Ecart Actuel/Signé")

    sale_cout_signe_col = fields.Monetary(string="Coleur: ")
    sale_cout_actuel_col = fields.Monetary(string="Coleur: ")
    sale_cout_actuel_signe_col = fields.Monetary(string="Coleur: ")
    # group 2
    sale_forfait_signe_nb = fields.Monetary(string="Forfait copie Signé")
    sale_forfait_actuel_nb = fields.Monetary(string="Forfait copie Actuel")
    sale_forfait_actuel_signe_nb = fields.Monetary(string="Ecart Actuel/Signé")

    sale_forfait_signe_col = fields.Monetary(string="Coleur: ")
    sale_forfait_actuel_col = fields.Monetary(string="Coleur: ")
    sale_forfait_actuel_signe_col = fields.Monetary(string="Coleur: ")
    # group 3
    sale_abonnement_service = fields.Monetary(string="Abonnement Service")
    sale_autre_frais        = fields.Monetary(string="Autre frais")



    def sale_marge_fuc(self):
        self.sale_marge = 0


