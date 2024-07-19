import pygame as pg

from Resources.Textures.dataset import player_sprite

from Systems.SubModules.move_mob import move_mob
from Systems.SubModules.attack_mob import attack_melee, attack_range


class PlayerSystem():
    def __init__(self, EntityManager):
        self.EM = EntityManager
        self.tile_map = self.EM.tile_map

        self.interactable_dict = self.EM.interactable_dict

        self.visible_mobs = self.EM.visible_mobs
        self.mobs_stats = self.EM.mobs_stats

    def try_move_player(self, tile_id):
        target_mob_id = self.tile_map[tile_id]['mob']
        players_tile = self.EM.mobs_stats[2].tile_id

        if target_mob_id == 2:
            print('try_move_player:', tile_id ,"is player's tile") #console_log
            return

        if target_mob_id == -1:
            print('try_move_player:', tile_id ,"is impossible") #console_log
            return

        if tile_id in self.tile_map[players_tile]['neighbors']:
            # move
            if target_mob_id == 0:
                if self.mobs_stats[2].is_movement_possable() == False:
                    print('try_move_player: no movement points left') #console_log
                    return
                move_mob(
                    destination_tile=tile_id, 
                    original_tile=players_tile, 
                    ent_id=2, 
                    tile_map=self.tile_map,
                    movement_cost=1,
                    mobs_stats=self.mobs_stats,
                    sprite=player_sprite
                    )
                print('move_player:', 'moved from', players_tile, 'to', tile_id) #console_log
                self.EM.update_visible()
                return
            # attack melee
            if self.mobs_stats[2].is_action_possable() == False:
                print('try_move_player: no action points left') #console_log
                return
            if self.mobs_stats[2].selected_weapon == None or hasattr(self.mobs_stats[2].selected_weapon, 'melee_damage'):
                attack_melee(self, 2, target_mob_id, tile_id)
            elif hasattr(self.mobs_stats[2].selected_weapon, 'range_damage'):
                attack_range(self, 2, target_mob_id, tile_id)
            else:
                print('!try_move_player: something wrong happend') #console_log
            return
            
        if target_mob_id != 0 and target_mob_id in self.EM.visible_mobs_ids:
            attack_range(self, 2, target_mob_id, tile_id)
            return

        print('try_move_player: tile', tile_id, 'is unreachable') #console_log
