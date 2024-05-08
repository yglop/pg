from Systems.EntitySystems.Entity.item import BaseItem

from Resources.Locale.locale import locale


class BaseLimb(BaseItem):
    def __init__(self):
        super().__init__()
        self.nutrition = 100
        self.limb_points = 1
        self.hand_points = 0
        self.movement_points = 0
        self.action_points = 0
        self.melee_damage = 0


## arms
class LimbArmHuman(BaseLimb):
    def __init__(self):
        super().__init__()
        self.name = locale['arm_human_name']
        self.limb_type = 'hand'
        self.max_health = 2
        self.health = 2

        self.hand_points = 1
        self.action_points = 1
        self.melee_damage = 1


class LimbArmBlade(BaseLimb):
    def __init__(self):
        super().__init__()
        self.name = locale['arm_blade_name']
        self.limb_type = 'hand'
        self.max_health = 2
        self.health = 2

        self.action_points = 1
        self.melee_damage = 6


## legs
class LimbLegHuman(BaseLimb):
    def __init__(self):
        super().__init__()
        self.name = locale['leg_human_name']
        self.limb_type = 'leg'
        self.max_health = 3
        self.health = 3
        
        self.movement_points = 1
