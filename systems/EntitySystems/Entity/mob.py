

class Mob():
    def __init__(self, data):
        self.tile_id = data['tile_id']

        self.max_actions = data['max_actions']
        self.actions = self.max_actions

        self.max_health = data['max_health']
        self.health = self.max_health

        self.melee_damage = 1

    def subtract_action(self, cost=1):
        self.actions -= cost

    def is_action_possable(self, cost=1):
        if self.actions >= cost:
            return True
        return False