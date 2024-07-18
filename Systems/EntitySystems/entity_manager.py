import pygame as pg
import random

from Systems.EntitySystems.player_system import PlayerSystem
from Systems.EntitySystems.enemy_system import EnemySystem
from Systems.EntitySystems.items_system import ItemSystem
from Systems.EntitySystems.raycast import raycast

from Systems.EntitySystems.Entity.mob import Mob
from Systems.EntitySystems.Entity.presets import *

from Visuals.mob_visual import MobVisual
from Resources.Textures.dataset import player_sprite, enemy_sprite


class EntityManager():
    def __init__(self, MS, SM):
        self.tile_map = MS.tile_map
        self.grid_size = MS.grid_size

        self.visible_mobs = pg.sprite.RenderPlain()
        self.visible_mobs_ids = list()
        self.mobs_stats = dict()
        self.interactable_dict = dict()
        self.interactable_id_count = 1000

        self.save_manager = SM

        self.PS = PlayerSystem(self) 
        self.ES = EnemySystem(self)
        self.IS = ItemSystem()

        self.iterate_through_tile_map()
        self.update_visible()

    def iterate_through_tile_map(self):
        for tile_id, tile_data in self.tile_map.items():
            mob_id = tile_data['mob']
            if mob_id == 2:
                self.append_mobs_stats(tile_id, mob_id)
            elif tile_data['mob'] >= 100:
                self.append_mobs_stats(tile_id, mob_id)
   
    def append_mobs_stats(self, tile_id, mob_id):
        _equipment_preset = None
        if mob_id == 2:
            self.save_manager.load_save()
            _equipment_preset = self.save_manager.player
        else:
            _equipment_preset = equipment_preset[random.choice(['humanA', 'humanB'])].copy()
        _equipment_preset['tile_id'] = tile_id
        self.mobs_stats[mob_id] = Mob(_equipment_preset)

    def create_mobs_visual(self):
        for mob_id in self.visible_mobs_ids:
            if mob_id == 2:
                sprite = player_sprite
            else:
                sprite = enemy_sprite

            tile_data = self.tile_map[self.mobs_stats[mob_id].tile_id]
            new_mob = MobVisual(sprite, tile_data['rect'], tile_data['rect.center'])
            self.visible_mobs.add(new_mob)

    def update_visible(self):
        self.visible_mobs.empty()
        self.visible_mobs_ids = raycast(self.tile_map, self.mobs_stats)
        self.create_mobs_visual()

    def render_ents(self, screen):
        self.visible_mobs.draw(screen)
