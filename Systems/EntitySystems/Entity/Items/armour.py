from Systems.EntitySystems.Entity.item import BaseItem


class ArmourP1(BaseItem):
    def __init__(self):
        super().__init__()
        self.name = 'BaseArmour'
        self.max_health = 10
        self.health = self.max_health
        self.protection = 1
