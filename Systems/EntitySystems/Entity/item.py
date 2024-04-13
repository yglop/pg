

class BaseItem():
    def __init__(self):
        self.space = 1

## Armour
class ArmourP1(BaseItem):
    def __init__(self):
        super().__init__()
        self.name = 'BaseArmour'
        self.protection = 1

## Limbs
class LimbHandHuman(BaseItem):
    def __init__(self):
        super().__init__()
        self.name = 'BaseLimb'
        self.limb_type = 'hand'

        self.limb_points = 1
        self.action_points = 0

        self.health = 1
        self.melee_damage = 2


class LimbLegHuman(BaseItem):
    def __init__(self):
        super().__init__()
        self.name = 'BaseLimb'
        self.limb_type = 'leg'
        
        self.limb_points = 1
        self.action_points = 1

        self.health = 1
        self.melee_damage = 0


class BaseOrgan(BaseItem):
    def __init__(self):
        self.name = 'BaseOrgan' 


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
