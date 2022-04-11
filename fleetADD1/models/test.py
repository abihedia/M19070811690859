@api.depends('fleet_date_inst')
@api.onchange('fleet_date_inst', 'fleet_duree', 'fleet_periodicite', 'fleet_expiration_date')
def duree_rest(self):
    if self.fleet_expiration_date:
        if self.fleet_expiration_date >= date.today():
            nombre_jour = date.today() - self.fleet_date_inst
            if self.fleet_periodicite == 'mens':
                self.fleet_duree_rest = nombre_jour.days / 30
            elif self.fleet_periodicite == 'trim':
                self.fleet_duree_rest = nombre_jour.days / 90
            else:
                self.fleet_duree_rest = 0
        else:
            if self.fleet_periodicite == 'mens':
                self.fleet_duree_rest = (self.fleet_expiration_date - self.date.today()).days / 30
            elif self.fleet_periodicite == 'trim':
                self.fleet_duree_rest = (self.fleet_expiration_date - self.date.today()).days / 90
            else:
                self.fleet_duree_rest = 0
    else:
        self.fleet_duree_rest = 0