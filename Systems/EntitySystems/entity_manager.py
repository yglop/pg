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

from copy import deepcopy


class EntityManager():
    def __init__(self, MS, SM):
        self.map_system = MS
        self.tile_map = self.map_system.tile_map
        self.grid_size = self.map_system.grid_size

        self.visible_mobs = pg.sprite.RenderPlain()
        self.visible_mobs_ids = list()
        self.mobs_stats = dict()
        self.visible_tiles = list()
        self.interactable_dict = dict()
        self.interactable_id_count = 1000

        self.save_manager = SM

        self.PS = PlayerSystem(self) 
        self.ES = EnemySystem(self)
        self.IS = ItemSystem()

        self.create_mobs_stats()
        self.update_visible()

    def create_mobs_stats(self):
        for tile_id, tile_data in self.tile_map.items():
            mob_id = tile_data['mob']
            _equipment_preset = None
            if mob_id == 2:
                self.save_manager.load_save()
                _equipment_preset = self.save_manager.player
            elif tile_data['mob'] >= 100:
                _equipment_preset = deepcopy(equipment_preset[random.choice(['humanA', 'humanB'])])
            else:
                continue
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

    def get_visible_tiles(self):
        self.visible_tiles.clear()
        player_tile = self.mobs_stats[2].tile_id

        OFFCET_MINUS = 6
        OFFCET_PLUS = OFFCET_MINUS + 1

        offcet00 = 0
        offcet01 = 0
        offcet10 = self.grid_size
        offcet11 = self.grid_size
        # 00
        if player_tile[0] - OFFCET_MINUS > 0:
            offcet00 = player_tile[0] - OFFCET_MINUS
        # 01
        if player_tile[1] - OFFCET_MINUS > 0:
            offcet01 = player_tile[1] - OFFCET_MINUS
        # 10
        if player_tile[0] + OFFCET_PLUS < self.grid_size:
            offcet10 = player_tile[0] + OFFCET_PLUS
        # 11
        if player_tile[1] + OFFCET_PLUS < self.grid_size:
            offcet11 = player_tile[1] + OFFCET_PLUS
        
        border_tile_0 = [offcet00, offcet01]
        border_tile_1 = [offcet10, offcet11]

        while border_tile_0[0] < border_tile_1[0]:
            while border_tile_0[1] < border_tile_1[1]:
                self.visible_tiles.append((border_tile_0[0], border_tile_0[1]))
                border_tile_0[1] += 1
            border_tile_0[0] += 1
            border_tile_0[1] = offcet01

    def update_visible(self):
        self.get_visible_tiles()
        self.map_system.create_tiles(self.visible_tiles)
        self.visible_mobs.empty()
        self.visible_mobs_ids = raycast(self.tile_map, self.visible_tiles, self.mobs_stats)
        self.create_mobs_visual()

    def render_ents(self, screen):
        self.visible_mobs.draw(screen)
