from Systems.EntitySystems.Entity.item import BaseItem


class ArmourP1(BaseItem):
    def __init__(self):
        super().__init__()
        self.name = 'BaseArmour'
        self.protection = 1
