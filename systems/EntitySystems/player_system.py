import pygame as pg

from visuals.display_ent import EntityVisual
from dataset import player_sprite


class PlayerSystem():
    def __init__(self, EntityManager):
        self.turn_system = EntityManager.turn_system
        self.tile_map = EntityManager.tile_map

        self.ent_visual_dict = EntityManager.ent_visual_dict
        self.ent_stats_dict = EntityManager.ent_stats_dict

    def player_melee_attack(self, destination_tile):
        target_ent = self.tile_map[destination_tile]['entity']
        if self.turn_system.current_player_actions > 0:
            self.turn_system.player_did_something(1)
            self.ent_stats_dict[target_ent].health -= 1
            print('player_melee_attack: player attacks', target_ent)
        if self.ent_stats_dict[target_ent].health <= 0:
            del self.ent_stats_dict[target_ent]
            del self.ent_visual_dict[target_ent]
            self.tile_map[destination_tile]['entity'] = 0
            print('player_melee_attack:', target_ent, 'died')
        else:
            print('player_melee_attack:', target_ent, 'hp=', self.ent_stats_dict[target_ent].health)

    def move_player(self, destination_tile, original_tile):
        destination = self.tile_map[destination_tile]
        origin = self.tile_map[original_tile]
        
        if destination['entity'] == 0:
            origin['entity'] = 0
            destination['entity'] = 2

            ent_new_sprite = EntityVisual(player_sprite, destination['rect'], destination['rect.center'])
            self.ent_visual_dict[destination['entity']] = pg.sprite.RenderPlain(ent_new_sprite)

            self.turn_system.player_did_something(1)
            print('move_player:', 'moved from', original_tile, 'to', destination_tile)
        else:
            self.player_melee_attack(destination_tile)
            #print('move_player:', destination_tile ,'is an enemy tile')

    def try_move_player(self, tile_id):
        if self.turn_system.is_action_possable() == False:
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
                self.move_player(tile_id, i)
                return
            
        print('try_move_player: tile', tile_id, 'is unreachable')
