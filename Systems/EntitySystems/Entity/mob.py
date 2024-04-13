

class Mob():
    def __init__(self, data):
        self.tile_id = data['tile_id']

        self.armour = data['armour']

        self.max_limb_points = 4
        self.limbs = data['limbs']

        self.max_actions = 1
        self.actions = self.max_actions

        self.max_health = 1
        self.health = self.max_health

        self.melee_damage = 1

        self.update_stats()

    def subtract_action(self, cost=1):
        self.actions -= cost

    def is_action_possable(self, cost=1):
        if self.actions >= cost:
            return True
        return False

    def update_stats(self):
        max_health = 0
        max_actions = 0
        melee_damage = 0

        for limb in self.limbs:
            max_health += limb.health
            max_actions += limb.action_points
            melee_damage += limb.melee_damage

        self.max_health = max_health
        self.health = self.max_health
        
        self.max_actions = max_actions
        self.actions = self.max_actions

        self.melee_damage = melee_damage
