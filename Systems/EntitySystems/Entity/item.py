

class BaseItem():
    def __init__(self):
        self.space = 1


class BaseWeaponRange(BaseItem):
    def __init__(self):
        self.name = 'BaseWeaponRange'


class BaseWeaponMelee(BaseItem):
    def __init__(self):
        self.name = 'BaseWeaponMelee'


class BaseLimb(BaseItem):
    def __init__(self):
        self.name = 'BaseLimb'


class BaseOrgan(BaseItem):
    def __init__(self):
        self.name = 'BaseOrgan' 


class BaseMutator(BaseItem):
    def __init__(self):
        self.name = 'BaseMutator' 


class BaseBrainImplant(BaseItem):
    def __init__(self):
        self.name = 'BaseBrainImplant' 