from Systems.EntitySystems.Entity.item import BaseItem

from Resources.Locale.locale import locale


class BaseOrgan(BaseItem):
    def __init__(self):
        super().__init__()
        self.nutrition = 100
        self.organ_points = 1
        self.organ_type = str()


## heart's
class HeartHuman(BaseOrgan):
    def __init__(self):
        super().__init__()
        self.name = locale['heart_human_name']
        self.max_health = 4 
        self.health = 4
        self.organ_type = 'heart'


## lungs
class LungsHuman(BaseOrgan):
    def __init__(self):
        super().__init__()
        self.name = locale['lungs_human_name']
        self.max_health = 4 
        self.health = 4
        self.organ_type = 'lungs'


## liver's
class LiverHuman(BaseOrgan):
    def __init__(self):
        super().__init__()
        self.name = locale['liver_human_name']
        self.max_health = 4 
        self.health = 4
        self.organ_type = 'liver'


## digestive systems
class DigestiveSystemHuman(BaseOrgan):
    def __init__(self):
        super().__init__()
        self.name = locale['digestive_system_human_name']
        self.max_health = 6
        self.health = 6
        self.organ_type = 'digestive'

