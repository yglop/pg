

class BaseItem():
    def __init__(self):
        self.name = 'BaseItem' 
        self.weight = 0
        self.health = 1


class BaseMutator(BaseItem):
    def __init__(self):
        self.name = 'BaseMutator' 


class BaseBrainImplant(BaseItem):
    def __init__(self):
        self.name = 'BaseBrainImplant' 

## Weapons
class BaseWeaponRange(BaseItem):
    def __init__(self):
        self.name = 'BaseWeaponRange'


class BaseWeaponMelee(BaseItem):
    def __init__(self):
        self.name = 'BaseWeaponMelee'
