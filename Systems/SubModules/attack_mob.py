import random

def attack_mob(target_part, target_mob, damage):
    if target_part == 'body':
        target_part = random.choice(target_mob.organs)
        if target_mob.armour:
            if damage > target_mob.armour.protection:
                target_part.health -= damage - target_mob.armour.protection
                target_mob.armour.health -= 1
            else:
                target_mob.armour.health -= damage
                target_part.health -= 1
            if target_mob.armour.health <= 0:
                target_mob.armour = None
        else:
            target_part.health -= damage
    else:
        target_part.health -= damage


def spawn_loot(data, target_mob, target_mob_id, destination, destination_tile):
    target_hearts = list()
    target_lungs = list()
    for organ in target_mob.organs:
        if organ.organ_type == 'heart' and organ.health > 0:
            target_hearts.append(organ)
        elif organ.organ_type == 'lungs' and organ.health > 0:
            target_lungs.append(organ)
        if organ.health <= 0:
            target_mob.organs.remove(organ)

    for limb in target_mob.limbs:
        if limb.health <= 0:
            target_mob.limbs.remove(limb)

    if len(target_hearts) == 0 or len(target_lungs) == 0:
        ## spawn/add loot
        loot = target_mob.limbs + target_mob.organs + target_mob.storage
        if target_mob.armour:
            loot.append(target_mob.armour)

        if destination['loot'] == 0:
            destination['loot'] = target_mob_id
            data.interactable_dict[target_mob_id] = loot
        else:
            data.interactable_dict[destination['loot']] += loot

        # delete ent
        del data.mobs_stats[target_mob_id]
        data.tile_map[destination_tile]['mob'] = 0

        data.EM.update_visible()

        print(f'attack: {target_mob.name} died')
    else:
        print(f'attack: {target_mob.name}')


def attack_melee(data, atatcker_mob_id, target_mob_id, destination_tile):
    atatcking_mob = data.mobs_stats[atatcker_mob_id]
    target_mob = data.mobs_stats[target_mob_id]
    destination = data.tile_map[destination_tile]

    if atatcking_mob.actions >= 1:
        atatcking_mob.subtract_action(1)

        targets_list = target_mob.limbs + ['body']
        target_part = random.choice(targets_list)
        if atatcking_mob.selected_weapon:
            attack_mob(target_part, target_mob, atatcking_mob.selected_weapon.melee_damage)
        else:
            attack_mob(target_part, target_mob, atatcking_mob.melee_damage)
        
        print(f'attack: {atatcking_mob.name} attacks {target_mob.name}')

        spawn_loot(data, target_mob, target_mob_id, destination, destination_tile)


def attack_range(data, atatcker_mob_id, target_mob_id, destination_tile):
    atatcking_mob = data.mobs_stats[atatcker_mob_id]
    target_mob = data.mobs_stats[target_mob_id]
    destination = data.tile_map[destination_tile]

    if atatcking_mob.actions >= 1 and hasattr(atatcking_mob.selected_weapon, 'range_damage'):
        atatcking_mob.subtract_action(1)

        targets_list = target_mob.limbs + ['body']
        target_part = random.choice(targets_list)
        attack_mob(target_part, target_mob, atatcking_mob.selected_weapon.range_damage)
        
        print(f'attack: {atatcking_mob.name} attacks {target_mob.name}')

        spawn_loot(data, target_mob, target_mob_id, destination, destination_tile)