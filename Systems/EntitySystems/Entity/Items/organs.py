from Systems.EntitySystems.Entity.item import BaseItem


class HeartHuman(BaseItem):
    def __init__(self):
        super().__init__()
        self.name = 'human heart' 
        self.health = 4
        
        self.blood_flow = 10


class LungsHuman(BaseItem):
    def __init__(self):
        super().__init__()
        self.name = 'human lungs' 
        self.health = 6
        
        self.oxidation = 10


class DigestiveSystemHuman(BaseItem):
    def __init__(self):
        super().__init__()
        self.name = 'human digestive system' 
        self.health = 8

