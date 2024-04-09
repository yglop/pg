import pygame as pg

from mapgen.map_gen import generate_map
from visuals.display_tile import TileVisual
from dataset import tile_sprites_32


class MapSystem():
    def __init__(self):
        self.grid_size = 30
        self.tile_map = dict() 
        self.group_tile = pg.sprite.RenderPlain()

        self.create_tile_map()
        self.create_tiles()

    def create_tile_map(self):
        game_map = generate_map(
            max_rooms=10,
            room_min_size=3,
            room_max_size=8,
            map_width=self.grid_size, 
            map_height=self.grid_size
            )

        tile_image_preset = {
            0: tile_sprites_32[1],
            1: tile_sprites_32[2],
            2: tile_sprites_32[2],
            8: tile_sprites_32[3],
            9: tile_sprites_32[2],
        }
        rile_ent_preset = {
            0: -1,
            1: 2,
            2: 100,
            8: 0,
            9: 0,
        }

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                pos_x = 32 + 32 * i
                pos_y = 32 + 32 * j
                           
                tile_image = tile_image_preset[game_map[i,j]]
                tile_ent = rile_ent_preset[game_map[i,j]]

                self.tile_map[(i,j)] = {
                    'image': tile_image,
                    'rect': tile_image.get_rect(),
                    'rect.center': (pos_x, pos_y),
                    'entity': tile_ent,
                    'neighbors': self.get_neighbors((i,j))
                }

        enemy_count = 1
        for tile_id, tile_data in self.tile_map.items():
            if tile_data['entity'] >= 100:
                enemy_count += 1
                self.tile_map[tile_id]['entity'] += enemy_count

    def create_tiles(self):
        for tile_id, tile_data in self.tile_map.items():  
            tile = [tile_id, tile_data]  
            new_tile = TileVisual(tile)

            self.group_tile.add(new_tile)

    def get_neighbors(self, tile_id):
        neighbors = set()
        #   @@@@
        #   @//@
        #   @//@
        #   @@@@
        if (
                (tile_id[0] > 0 and tile_id[0] < self.grid_size) and
                (tile_id[1] > 0 and tile_id[1] < self.grid_size)
            ):
            neighbors = (
                (tile_id[0]+1, tile_id[1]+0), 
                (tile_id[0]+0, tile_id[1]+1), 
                (tile_id[0]-1, tile_id[1]+0), 
                (tile_id[0]+0, tile_id[1]-1), 
                (tile_id[0]+1, tile_id[1]+1), 
                (tile_id[0]-1, tile_id[1]-1), 
                (tile_id[0]+1, tile_id[1]-1), 
                (tile_id[0]-1, tile_id[1]+1), 
            )
        #   @//@
        #   @@@@
        #   @@@@
        #   @@@@
        elif (
                (tile_id[0] == 0) and
                (tile_id[1] > 0 and tile_id[1] < self.grid_size)
            ):
            neighbors = (
                (tile_id[0]+1, tile_id[1]+0), 
                (tile_id[0]+0, tile_id[1]+1), 
                (tile_id[0]+0, tile_id[1]-1),
                (tile_id[0]+1, tile_id[1]+1),
                (tile_id[0]+1, tile_id[1]-1),
            )
        #   @@@@
        #   @@@@
        #   @@@@
        #   @//@
        elif (
                (tile_id[0] == self.grid_size) and
                (tile_id[1] > 0 and tile_id[1] < self.grid_size)
            ):
            neighbors = (
                (tile_id[0]-1, tile_id[1]+0), 
                (tile_id[0]+0, tile_id[1]+1), 
                (tile_id[0]+0, tile_id[1]-1),
                (tile_id[0]-1, tile_id[1]-1),
                (tile_id[0]-1, tile_id[1]+1),
            )
        #   @@@@
        #   @@@/
        #   @@@/
        #   @@@@
        elif (
                (tile_id[0] > 0 and tile_id[0] < self.grid_size) and
                (tile_id[1] == self.grid_size)
            ):
            neighbors = (
                (tile_id[0]+1, tile_id[1]+0), 
                (tile_id[0]-1, tile_id[1]+0), 
                (tile_id[0]+0, tile_id[1]-1),
                (tile_id[0]+1, tile_id[1]-1),
                (tile_id[0]-1, tile_id[1]-1),
            )
        #   @@@@
        #   /@@@
        #   /@@@
        #   @@@@
        elif (
                (tile_id[0] > 0 and tile_id[0] < self.grid_size) and
                (tile_id[1] == 0)
            ):
            neighbors = (
                (tile_id[0]+1, tile_id[1]+0), 
                (tile_id[0]-1, tile_id[1]+0), 
                (tile_id[0]+0, tile_id[1]+1),
                (tile_id[0]+1, tile_id[1]+1),
                (tile_id[0]-1, tile_id[1]+1),
            )
        #   /@@@
        #   @@@@
        #   @@@@
        #   @@@@
        elif (
                (tile_id[0] == 0) and
                (tile_id[1] == 0)
            ):
            neighbors = (
                (tile_id[0]+1, tile_id[1]+0), 
                (tile_id[0]+0, tile_id[1]+1), 
                (tile_id[0]+1, tile_id[1]+1),
            )
        #   @@@/
        #   @@@@
        #   @@@@
        #   @@@@
        elif (
                (tile_id[0] == 0) and
                (tile_id[1] == self.grid_size)
            ):
            neighbors = (
                (tile_id[0]+1, tile_id[1]+0), 
                (tile_id[0]+0, tile_id[1]-1), 
                (tile_id[0]+1, tile_id[1]-1),
            )
        #   @@@@
        #   @@@@
        #   @@@@
        #   /@@@
        elif (
                (tile_id[0] == self.grid_size) and
                (tile_id[1] == 0)
            ):
            neighbors = (
                (tile_id[0]-1, tile_id[1]+0), 
                (tile_id[0]+0, tile_id[1]+1), 
                (tile_id[0]-1, tile_id[1]+1),
            )
        #   @@@@
        #   @@@@
        #   @@@@
        #   @@@/
        elif (
                (tile_id[0] == self.grid_size) and
                (tile_id[1] == self.grid_size)
            ):
            neighbors = (
                (tile_id[0]-1, tile_id[1]-0), 
                (tile_id[0]-0, tile_id[1]-1), 
                (tile_id[0]-1, tile_id[1]-1),
            )
            
        return neighbors
