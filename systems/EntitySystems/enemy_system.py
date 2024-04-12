import pygame as pg
import random

from visuals.display_ent import EntityVisual
from Resources.Textures.dataset import enemy_sprite


class EnemySystem():
    def __init__(self, EntityManager):
        self.tile_map = EntityManager.tile_map

        self.ent_visual_dict = EntityManager.ent_visual_dict
        self.ent_stats_dict = EntityManager.ent_stats_dict


    def move_enemy(self, ent_id, movement_cost, directions):
        movement_direction = random.choice(directions)

        destination = self.tile_map[movement_direction]
        original_tile = self.ent_stats_dict[ent_id].tile_id

        self.tile_map[original_tile]['entity'] = 0
        destination['entity'] = ent_id

        self.ent_stats_dict[ent_id].subtract_action(movement_cost)
        self.ent_stats_dict[ent_id].tile_id = movement_direction

        ent_new_sprite = EntityVisual(enemy_sprite, destination['rect'], destination['rect.center'])
        self.ent_visual_dict[destination['entity']] = pg.sprite.RenderPlain(ent_new_sprite)

        print('move_enemy:', ent_id, 'moved from to', movement_direction)

    def try_move_enemy(self, ent_id):
        movement_cost = 1
        while self.ent_stats_dict[ent_id].actions >= movement_cost:
            original_tile = self.ent_stats_dict[ent_id].tile_id
            directions = list()
            for i in self.tile_map[original_tile]['neighbors']:
                if self.tile_map[i]['entity'] == 0:
                    directions.append(i)

            if len(directions) == 0:
                print('try_move_enemy: no possuble direction')
                return

            self.move_enemy(ent_id, movement_cost, directions)

        
            
