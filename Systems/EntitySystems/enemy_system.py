import pygame as pg
import random

from Resources.Textures.dataset import enemy_sprite

from Systems.SubModules.move_mob import move_mob


class EnemySystem():
    def __init__(self, EntityManager):
        self.EM = EntityManager
        self.tile_map = self.EM.tile_map

        self.visible_mobs = self.EM.visible_mobs
        self.mobs_stats = self.EM.mobs_stats

    def try_move_enemy(self, ent_id):
        movement_cost = 1
        mob = self.mobs_stats[ent_id]
        while mob.movements >= movement_cost:
            original_tile = mob.tile_id
            directions = list()
            for i in self.tile_map[original_tile]['neighbors']:
                if self.tile_map[i]['mob'] == 0:
                    directions.append(i)

            if len(directions) == 0:
                print('try_move_enemy: no possuble direction') #console_log
                return

            move_mob(
                    destination_tile=random.choice(directions), 
                    original_tile=mob.tile_id, 
                    ent_id=ent_id, 
                    tile_map=self.tile_map,
                    movement_cost=movement_cost,
                    mobs_stats=self.mobs_stats,
                    sprite=enemy_sprite
                    )
            
