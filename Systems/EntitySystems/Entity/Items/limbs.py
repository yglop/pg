from Systems.EntitySystems.Entity.item import BaseItem


class BaseLimb(BaseItem):
    def __init__(self):
        super().__init__()
        self.limb_points = 1
        self.action_points = 0
        self.melee_damage = 0


## arms
class LimbArmHuman(BaseLimb):
    def __init__(self):
        super().__init__()
        self.name = 'human arm'
        self.limb_type = 'hand'
        self.health = 2

        self.melee_damage = 1


class LimbArmBlade(BaseLimb):
    def __init__(self):
        super().__init__()
        self.name = 'armblade'
        self.limb_type = 'hand'
        self.health = 2

        self.melee_damage = 6


## legs
class LimbLegHuman(BaseLimb):
    def __init__(self):
        super().__init__()
        self.name = 'human leg'
        self.limb_type = 'leg'
        self.health = 3
        
        self.action_points = 1
