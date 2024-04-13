

class Mob():
    def __init__(self, data):
        self.tile_id = data['tile_id']
        self.name = data['name']

        self.armour = data['armour']

        self.max_limb_points = 4
        self.limbs = data['limbs']

        self.max_organ_points = 4
        self.organs = data['organs']

        self.max_actions = 1
        self.max_health = 1
        self.melee_damage = 1
        self.weight = 1

        self.update_stats()

        self.actions = self.max_actions
        self.health = self.max_health

    def subtract_action(self, cost=1):
        self.actions -= cost

    def is_action_possable(self, cost=1):
        if self.actions >= cost:
            return True
        return False

    def attack(self, data, target_mob_id, destination_tile):
        target_mob = data.mobs_stats[target_mob_id]
        destination = data.tile_map[destination_tile]

        if self.actions >= self.weight:
            #attaker_mob.attack(target_mob)
            self.subtract_action(self.weight)
            if self.melee_damage > target_mob.armour.protection:
                target_mob.health -= self.melee_damage - target_mob.armour.protection
            else:
                target_mob.health -= 1
            print(f'attack: {self.name} attacks {target_mob.name}')
        if target_mob.health <= 0:
            ## spawn/add loot to {interactable} 
            if destination['interactable'] == 0:
                destination['interactable'] = target_mob_id
                data.interactable_dict[target_mob_id] = [10_005, 10_006]
            else:
                data.interactable_dict[destination['interactable']] += [10_105, 10_106]

            # delete ent
            del data.mobs_stats[target_mob_id]
            del data.mobs_visual[target_mob_id]
            data.tile_map[destination_tile]['mob'] = 0

            print(f'attack: {target_mob.name} died')
        else:
            print(f'attack: {target_mob.name} hp={target_mob.health}')

    def update_stats(self):
        max_health = 0
        max_actions = 0
        melee_damage = 0
        weight = 1

        for limb in self.limbs:
            max_health += limb.health
            max_actions += limb.action_points
            melee_damage += limb.melee_damage
            weight += limb.weight

        self.max_health = max_health
        self.max_actions = max_actions
        self.melee_damage = melee_damage
        self.weight = weight
