from Systems.EntitySystems.Entity.item import BaseItem

from Resources.Locale.locale import locale


class BaseWeaponMelee(BaseItem):
    def __init__(self):
        super().__init__()
        self.hands_required = 1
        self.melee_damage = 1
        

class Sword(BaseWeaponMelee):
    def __init__(self):
        super().__init__()
        self.name = locale['weapon_melee_sword']