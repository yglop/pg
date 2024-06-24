from Systems.EntitySystems.Entity.Items.weapons_melee import *
from Systems.EntitySystems.Entity.Items.weapons_range import *


class Mission():
    def __init__(self, name='test mission', ):
        self.name = name

        self.reward = [Pistol(), Sword()]
        self.rep_change = [1, 1, 1, 1]
        self.condition = None