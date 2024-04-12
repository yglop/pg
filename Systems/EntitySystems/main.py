import pygame as pg

from Systems.EntitySystems.player_system import PlayerSystem
from Systems.EntitySystems.enemy_system import EnemySystem
from Systems.EntitySystems.items_system import ItemSystem

from Systems.EntitySystems.Entity.mob import Mob

from Visuals.display_ent import EntityVisual
from Resources.Textures.dataset import player_sprite, enemy_sprite


class EntityManager():
    def __init__(self, MS):
        self.tile_map = MS.tile_map
        self.grid_size = MS.grid_size

        self.ent_visual_dict = dict()
        self.ent_stats_dict = dict()

        self.PS = PlayerSystem(self) 
        self.ES = EnemySystem(self)
        self.IS = ItemSystem()

        self.iterate_through_tile_map()

    def iterate_through_tile_map(self):
        for tile_id, tile_data in self.tile_map.items():
            if tile_data['entity'] == 2:
                self.append_ent_visual_dict(tile_data, sprite=player_sprite)
                self.append_ent_stats_dict(tile_id, ent_id=tile_data['entity'])
            elif tile_data['entity'] >= 100:
                self.append_ent_visual_dict(tile_data, sprite=enemy_sprite)
                self.append_ent_stats_dict(tile_id, ent_id=tile_data['entity'])
    
    def append_ent_visual_dict(self, tile_data, sprite):
        new_ent = EntityVisual(sprite, tile_data['rect'], tile_data['rect.center'])
        self.ent_visual_dict[tile_data['entity']] = pg.sprite.RenderPlain(new_ent)
   
    def append_ent_stats_dict(self, tile_id, ent_id):
        if ent_id == 2:
            self.ent_stats_dict[ent_id] = Mob({'max_actions':2,'max_health':10,'tile_id':tile_id})
        else:
            self.ent_stats_dict[ent_id] = Mob({'max_actions':1,'max_health':2,'tile_id':tile_id})
    
    def render_ents(self, screen):
        for ent_id, ent_visual in self.ent_visual_dict.items():
            ent_visual.draw(screen)
