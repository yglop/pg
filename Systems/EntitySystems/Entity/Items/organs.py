from Systems.EntitySystems.Entity.item import BaseItem


class BaseOrgan(BaseItem):
    def __init__(self):
        super().__init__()
        self.nutrition = 100
        self.organ_points = 2
        self.critical = False


## critical systems
class CriticalSystemsHuman(BaseOrgan):
    def __init__(self):
        super().__init__()
        self.name = 'human critical sys'
        self.max_health = 4 
        self.health = 4
        
        self.critical = True


class CriticalSystemsChangeling(BaseOrgan):
    def __init__(self):
        super().__init__()
        self.name = 'ling critical sys' 
        self.max_health = 6
        self.health = 6
        
        self.critical = True


## digestive systems
class DigestiveSystemHuman(BaseOrgan):
    def __init__(self):
        super().__init__()
        self.name = 'human digestive sys' 
        self.max_health = 6
        self.health = 6


