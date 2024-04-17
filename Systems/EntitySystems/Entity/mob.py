import random



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
        self.melee_damage = 1

        self.max_storage_capacity = 5
        self.storage_capacity = 0
        self.storage = list()

        self.update_stats()

        self.actions = self.max_actions

    def subtract_action(self, cost=1):
        self.actions -= cost

    def is_action_possable(self, cost=1):
        if self.actions >= cost:
            return True
        return False

    def attack(self, data, target_mob_id, destination_tile):
        target_mob = data.mobs_stats[target_mob_id]
        destination = data.tile_map[destination_tile]

        if self.actions >= 1:
            self.subtract_action(1)

            targets_list = target_mob.limbs + ['body']
            target_part = random.choice(targets_list)
            if target_part == 'body':
                target_part = random.choice(target_mob.organs)
                if self.melee_damage > target_mob.armour.protection:
                    target_part.health -= self.melee_damage - target_mob.armour.protection
                else:
                    target_mob.armour.health -= self.melee_damage
                    target_part.health -= 1
            else:
                target_part.health -= self.melee_damage
            print(f'attack: {self.name} attacks {target_mob.name}')
        
        target_critical_organs = list()
        for organ in target_mob.organs:
            if organ.critical == True and organ.health > 0:
                target_critical_organs.append(organ)
            elif organ.health <= 0:
                target_mob.organs.remove(organ)

        for limb in target_mob.limbs:
            if limb.health <= 0:
                target_mob.limbs.remove(limb)

        if len(target_critical_organs) == 0:
            ## spawn/add loot to {interactable} 
            if destination['interactable'] == 0:
                destination['interactable'] = target_mob_id
                data.interactable_dict[target_mob_id] = target_mob.limbs + target_mob.organs + target_mob.storage
            else:
                data.interactable_dict[destination['interactable']] += target_mob.limbs + target_mob.organs + target_mob.storage

            # delete ent
            del data.mobs_stats[target_mob_id]
            del data.mobs_visual[target_mob_id]
            data.tile_map[destination_tile]['mob'] = 0

            print(f'attack: {target_mob.name} died')
        else:
            print(f'attack: {target_mob.name}')

    def update_stats(self):
        max_actions = 0
        melee_damage = 0
        used_limb_points = 0
        used_organ_points = 0
        storage_capacity = 0

        for limb in self.limbs:
            max_actions += limb.action_points
            melee_damage += limb.melee_damage
            used_limb_points += limb.limb_points

        for organ in self.organs:
            used_organ_points += organ.organ_points

        for i in self.storage:
            storage_capacity += i.weight

        self.max_actions = max_actions
        self.melee_damage = melee_damage
        self.used_limb_points = used_limb_points
        self.used_organ_points = used_organ_points
        self.storage_capacity = storage_capacity
