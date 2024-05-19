


class Mob():
    def __init__(self, data):
        self.tile_id = data['tile_id']
        self.name = data['name']

        self.armour = data['armour']

        self.max_limb_points = 4
        self.used_limb_points = 0
        self.limbs = data['limbs']

        self.max_organ_points = 4
        self.used_organ_points = 0
        self.organs = data['organs']

        self.max_nutrition = 1000
        self.nutrition = 1000

        self.max_actions = 1
        self.max_movements = 1
        self.melee_damage = 1

        self.hands = 0
        self.used_hands = 0
        self.in_hands = list()
        self.selected_weapon = None

        self.max_storage_capacity = 5
        self.storage_capacity = 0
        self.storage = data['storage']

        self.update_stats()

        self.actions = self.max_actions
        self.movements = self.max_movements

    def subtract_action(self, cost=1):
        self.actions -= cost

    def is_action_possable(self, cost=1):
        if self.actions >= cost:
            return True
        return False

    def subtract_movement(self, cost=1):
        self.movements -= cost

    def is_movement_possable(self, cost=1):
        if self.movements >= cost:
            return True
        return False

    def update_stats(self):
        max_actions = 0
        max_movements = 0
        melee_damage = 0
        used_limb_points = 0
        used_organ_points = 0
        hands = 0
        used_hands = 0
        storage_capacity = 0

        for limb in self.limbs:
            max_actions += limb.action_points
            max_movements += limb.movement_points
            melee_damage += limb.melee_damage
            used_limb_points += limb.limb_points
            hands += limb.hand_points

        for organ in self.organs:
            used_organ_points += organ.organ_points

        for weapon in self.in_hands:
            used_hands += weapon.hands_required

        for i in self.storage:
            storage_capacity += i.weight

        self.max_actions = max_actions
        self.max_movements = max_movements
        self.melee_damage = melee_damage
        self.used_limb_points = used_limb_points
        self.used_organ_points = used_organ_points
        self.hands = hands
        self.used_hands = used_hands
        self.storage_capacity = storage_capacity
