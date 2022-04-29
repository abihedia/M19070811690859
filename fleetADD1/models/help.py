"""


    @api.depends('fleet_date_inst')
    @api.onchange('fleet_date_inst', 'fleet_duree', 'fleet_periodicite', 'fleet_expiration_date')
    def duree_rest(self):
        if self.fleet_expiration_date:
            if self.fleet_expiration_date >= date.today():
                nombre_jour = date.today() - self.fleet_date_inst
                if self.fleet_periodicite == 'mens':
                    self.fleet_duree_rest = math.ceil(nombre_jour.days / 30)
                elif self.fleet_periodicite == 'trim':
                    self.fleet_duree_rest = math.ceil(nombre_jour.days / 90)
                else:
                    self.fleet_duree_rest = 0
            else:
                if self.fleet_periodicite == 'mens':
                    self.fleet_duree_rest = math.ceil((self.fleet_expiration_date - self.fleet_date_inst).days / 30)
                elif self.fleet_periodicite == 'trim':
                    self.fleet_duree_rest = math.ceil((self.fleet_expiration_date - self.fleet_date_inst).days / 90)
                else:
                    self.fleet_duree_rest = 0
        else:
            self.fleet_duree_rest = 0
from datetime import timedelta
from datetime import datetime
from dateutil import relativedelta
date1 = datetime.strptime(str('2020-1-01'), '%Y-%m-%d')-timedelta(days=1)
date2 = datetime.strptime(str('2025-3-31'), '%Y-%m-%d')
num_months = (date2.year - date1.year) * 12 +(date2.month - date1.month)
given_date = '2/1/2020'
print('Give Date: ', given_date)
date_format = '%d/%m/%Y'
dtObj = datetime.strptime(given_date, date_format)
# Add 20 months to a given datetime object
n = 63
future_date = dtObj + relativedelta(months=n)-relativedelta(days=1)

print('Date after 63 months: ', future_date.date())

##################################################################last calcul
    @api.depends('fleet_expiration_date')
    @api.onchange('fleet_date_inst', 'fleet_duree', 'fleet_periodicite', 'fleet_expiration_date')
    def duree_rest(self):
        if self.fleet_expiration_date:
            if self.fleet_expiration_date > date.today():
                if self.fleet_periodicite == 'mens':
                    self.fleet_duree_rest = math.floor((self.fleet_expiration_date - date.today()).days / 30)
                elif self.fleet_periodicite == 'trim':
                    self.fleet_duree_rest = math.floor((self.fleet_expiration_date - date.today()).days / 90)
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
##################################################################

"""