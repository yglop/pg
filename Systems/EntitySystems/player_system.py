import pygame as pg

from Resources.Textures.dataset import player_sprite

from Systems.SubModules.move_mob import move_mob


class PlayerSystem():
    def __init__(self, EntityManager):
        self.tile_map = EntityManager.tile_map

        self.ent_visual_dict = EntityManager.ent_visual_dict
        self.ent_stats_dict = EntityManager.ent_stats_dict

    def player_melee_attack(self, destination_tile):
        target_ent = self.tile_map[destination_tile]['entity']
        if self.ent_stats_dict[2].actions > 0:
            self.ent_stats_dict[2].subtract_action(1)
            self.ent_stats_dict[target_ent].health -= 1
            print('player_melee_attack: player attacks', target_ent)
        if self.ent_stats_dict[target_ent].health <= 0:
            del self.ent_stats_dict[target_ent]
            del self.ent_visual_dict[target_ent]
            self.tile_map[destination_tile]['entity'] = 0
            print('player_melee_attack:', target_ent, 'died')
        else:
            print('player_melee_attack:', target_ent, 'hp=', self.ent_stats_dict[target_ent].health)

    def try_move_player(self, tile_id):
        if self.ent_stats_dict[2].is_action_possable() == False:
            print('try_move_player: no actons points left')
            return

        if self.tile_map[tile_id]['entity'] == 2:
            print('try_move_player:', tile_id ,"is player's tile")
            return

        if self.tile_map[tile_id]['entity'] == -1:
            print('try_move_player:', tile_id ,"is impossible")
            return

        for i in self.tile_map[tile_id]['neighbors']:
            if self.tile_map[i]['entity'] == 2:
                if self.tile_map[tile_id]['entity'] == 0:
                    move_mob(
                        destination_tile=tile_id, 
                        original_tile=i, 
                        ent_id=2, 
                        tile_map=self.tile_map,
                        movement_cost=1,
                        ent_stats_dict=self.ent_stats_dict,
                        ent_visual_dict=self.ent_visual_dict,
                        sprite=player_sprite
                        )
                    print('move_player:', 'moved from', i, 'to', tile_id)
                    return
                self.player_melee_attack(tile_id)
                return
            
        print('try_move_player: tile', tile_id, 'is unreachable')
