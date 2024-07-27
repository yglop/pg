import pygame as pg
import random

from mapgen.mapgen import mapgen
from Systems.SubModules.get_neighbors import get_neighbors

from Visuals.tile_visual import TileVisual
from Resources.Textures.dataset import tile_sprites_32


class MapSystem():
    def __init__(self):
        self.tile_map = dict() 
        self.group_tile = pg.sprite.RenderPlain()

        self.mapgen = mapgen()
        self.grid_size = self.mapgen.MAP_SIZE
        self.mapgen.create_map()

        self.create_tile_map()
        self.set_entd_ids()
        #self.create_tiles()

    def create_tile_map(self):
        game_map = self.mapgen.str_map

        tile_image_preset = {
            '#': tile_sprites_32[1],
            '!': tile_sprites_32[2],
            '.': tile_sprites_32[2],
            ',': tile_sprites_32[3],
        }
        tile_ent_preset = {
            '#': -1,
            '!': 2,
            '.': 100,
            ',': 0, 
        }

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                pos_x = 32 + 32 * i
                pos_y = 32 + 32 * j
                           
                tile_image = tile_image_preset[game_map[i,j]]
                tile_ent = tile_ent_preset[game_map[i,j]]

                self.tile_map[(i,j)] = {
                    'image': tile_image,
                    'rect': tile_image.get_rect(),
                    'rect.center': (pos_x, pos_y),
                    'mob': tile_ent,
                    'loot': 0,
                    'neighbors': get_neighbors(self.grid_size-1, (i,j))
                }

    def set_entd_ids(self):
        enemy_count = 1
        for tile_id, tile_data in self.tile_map.items():
            if tile_data['mob'] >= 100:
                chose_enemy = random.choice([0,0,0,0,0,0,0,0,0,0,0,0,0,100]) # 1/14
                if chose_enemy == 0:
                    tile_data['mob'] = 0
                    continue
                enemy_count += 1
                self.tile_map[tile_id]['mob'] += enemy_count

    def create_tiles(self, visible_tiles):
        self.group_tile.empty()

        for tile_id in visible_tiles:
            tile = [tile_id, self.tile_map[tile_id]]  

            x = tile_id[0] - visible_tiles[0][0]
            y = tile_id[1] - visible_tiles[0][1]

            pos_x = 256 + 32 * x
            pos_y = 256 + 32 * y

            tile[1]['rect.center'] = (pos_x, pos_y)

            new_tile = TileVisual(tile)

            self.group_tile.add(new_tile)

