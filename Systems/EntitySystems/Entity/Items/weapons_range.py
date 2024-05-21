from Systems.EntitySystems.Entity.item import BaseItem

from Resources.Locale.locale import locale


class BaseWeaponRange(BaseItem):
    def __init__(self):
        super().__init__()
        self.hands_required = 1
        self.range_damage = 3
        

class Pistol(BaseWeaponRange):
    def __init__(self):
        super().__init__()
        self.name = locale['weapon_range_pistol']