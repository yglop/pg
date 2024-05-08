import random

def attack(data, atatcker_mob_id, target_mob_id, destination_tile):
    atatcking_mob = data.mobs_stats[atatcker_mob_id]
    target_mob = data.mobs_stats[target_mob_id]
    destination = data.tile_map[destination_tile]

    if atatcking_mob.actions >= 1:
        atatcking_mob.subtract_action(1)

        targets_list = target_mob.limbs + ['body']
        target_part = random.choice(targets_list)
        if target_part == 'body':
            target_part = random.choice(target_mob.organs)
            if target_mob.armour:
                if atatcking_mob.melee_damage > target_mob.armour.protection:
                    target_part.health -= atatcking_mob.melee_damage - target_mob.armour.protection
                else:
                    target_mob.armour.health -= atatcking_mob.melee_damage
                    target_part.health -= 1
            else:
                target_part.health -= atatcking_mob.melee_damage
        else:
            target_part.health -= atatcking_mob.melee_damage
        print(f'attack: {atatcking_mob.name} attacks {target_mob.name}')
    
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
        del data.mobs_visual[target_mob_id]
        data.tile_map[destination_tile]['mob'] = 0

        print(f'attack: {target_mob.name} died')
    else:
        print(f'attack: {target_mob.name}')
