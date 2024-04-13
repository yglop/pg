import pygame as pg
import random

from Resources.Textures.dataset import enemy_sprite

from Systems.SubModules.move_mob import move_mob


class EnemySystem():
    def __init__(self, EntityManager):
        self.tile_map = EntityManager.tile_map

        self.mobs_visual = EntityManager.mobs_visual
        self.mobs_stats = EntityManager.mobs_stats

    def try_move_enemy(self, ent_id):
        movement_cost = 1
        while self.mobs_stats[ent_id].actions >= movement_cost:
            original_tile = self.mobs_stats[ent_id].tile_id
            directions = list()
            for i in self.tile_map[original_tile]['neighbors']:
                if self.tile_map[i]['entity'] == 0:
                    directions.append(i)

            if len(directions) == 0:
                print('try_move_enemy: no possuble direction')
                return

            move_mob(
                    destination_tile=random.choice(directions), 
                    original_tile=self.mobs_stats[ent_id].tile_id, 
                    ent_id=ent_id, 
                    tile_map=self.tile_map,
                    movement_cost=movement_cost,
                    mobs_stats=self.mobs_stats,
                    mobs_visual=self.mobs_visual,
                    sprite=enemy_sprite
                    )


        
            
