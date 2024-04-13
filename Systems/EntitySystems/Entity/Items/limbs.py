from Systems.EntitySystems.Entity.item import BaseItem


class LimbHandHuman(BaseItem):
    def __init__(self):
        super().__init__()
        self.name = 'human hand'
        self.limb_type = 'hand'
        self.health = 1

        self.limb_points = 1
        self.action_points = 0

        self.melee_damage = 2


class LimbLegHuman(BaseItem):
    def __init__(self):
        super().__init__()
        self.name = 'human leg'
        self.limb_type = 'leg'
        self.health = 1
        
        self.limb_points = 1
        self.action_points = 1

        self.melee_damage = 0