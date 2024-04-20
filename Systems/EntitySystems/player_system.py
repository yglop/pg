import pygame as pg

from Resources.Textures.dataset import player_sprite

from Systems.SubModules.move_mob import move_mob
from Systems.SubModules.attack_mob import attack

class PlayerSystem():
    def __init__(self, EntityManager):
        self.tile_map = EntityManager.tile_map

        self.interactable_dict = EntityManager.interactable_dict

        self.mobs_visual = EntityManager.mobs_visual
        self.mobs_stats = EntityManager.mobs_stats

    def try_move_player(self, tile_id):
        if self.mobs_stats[2].is_action_possable() == False:
            print('try_move_player: no actons points left')
            return

        if self.tile_map[tile_id]['mob'] == 2:
            print('try_move_player:', tile_id ,"is player's tile")
            return

        if self.tile_map[tile_id]['mob'] == -1:
            print('try_move_player:', tile_id ,"is impossible")
            return

        for i in self.tile_map[tile_id]['neighbors']:
            if self.tile_map[i]['mob'] == 2:
                if self.tile_map[tile_id]['mob'] == 0:
                    move_mob(
                        destination_tile=tile_id, 
                        original_tile=i, 
                        ent_id=2, 
                        tile_map=self.tile_map,
                        movement_cost=1,
                        mobs_stats=self.mobs_stats,
                        mobs_visual=self.mobs_visual,
                        sprite=player_sprite
                        )
                    print('move_player:', 'moved from', i, 'to', tile_id)
                    return
                # attack
                target_mob_id = self.tile_map[tile_id]['mob']
                attack(self, 2, target_mob_id, tile_id)
                return
            
        print('try_move_player: tile', tile_id, 'is unreachable')
