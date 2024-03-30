import pygame as pg
import random

from display_tile import TileDisplayer
from display_ent import MySprite
from dataset import *

class DoEvrything():
    def __init__(self):
        self.grid_size = 5
        self.group_tile = pg.sprite.RenderPlain()
        self.group_ent = dict()
        self.tile_map = dict() 
        self.create_tile_map()
        self.create_ent()
        self.create_tiles()

    def create_tile_map(self):
        tile_ids = list()
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                tile_ids.append((i,j))     

        for i in tile_ids:
            tile_image = random.choice(tile_sprites)

            pos_x = 32 + 64 * i[0]
            pos_y = 32 + 64 * i[1]
            
            self.tile_map[i] = {
                'image': tile_image,
                'rect': tile_image.get_rect(),
                'rect.center': (pos_x, pos_y),
                'entity': 0,
                }
    
    def create_ent(self):
        # player
        center = self.grid_size // 2
        self.tile_map[(center, center)]['entity'] = 2 
        # enemy

        ## visuals
        for tile_id, tile_data in self.tile_map.items():
            if tile_data['entity'] != 0:
                new_ent = MySprite(player_sprite, tile_data['rect'], tile_data['rect.center'])
                self.group_ent[tile_data['entity']] = pg.sprite.RenderPlain(new_ent)

    def create_tiles(self):
        for tile_id, tile_data in self.tile_map.items():  
            tile = [tile_id, tile_data]  
            new_tile = TileDisplayer(tile)

            self.group_tile.add(new_tile)

    def move_player(self, destination_tile, original_tile):
        if self.tile_map[destination_tile]['entity'] != 1:
            self.tile_map[original_tile]['entity'] = 0
            self.tile_map[destination_tile]['entity'] = 2

            update_ent_pos = MySprite(player_sprite, self.tile_map[destination_tile]['rect'], self.tile_map[destination_tile]['rect.center'])
            self.group_ent[self.tile_map[destination_tile]['entity']] = pg.sprite.RenderPlain(update_ent_pos)

            print('move_player:', 'move from', original_tile, 'to', destination_tile)
        else:
            print(destination_tile ,'is enamy tile')

    # dont look at this PLEASE
    def try_move_player(self, tile=(0,0)):
        if self.tile_map[tile]['entity'] == 2:
            print('try_move_player:', tile ,'is player tile')

        if (tile[0] + 1 < self.grid_size and 
                self.tile_map[(tile[0] + 1, tile[1])]['entity'] == 2):
            self.move_player(tile, (tile[0] + 1, tile[1]))
        elif (tile[0] - 1 >= 0  and 
                self.tile_map[(tile[0] - 1, tile[1])]['entity'] == 2):
            self.move_player(tile, (tile[0] - 1, tile[1]))
        elif (tile[1] + 1 < self.grid_size and 
                self.tile_map[(tile[0], tile[1] + 1)]['entity'] == 2):
            self.move_player(tile, (tile[0], tile[1] + 1))
        elif (tile[1] - 1 >= 0 and 
                self.tile_map[(tile[0], tile[1] - 1)]['entity'] == 2):
            self.move_player(tile, (tile[0], tile[1] - 1))
        elif (tile[0] + 1 < self.grid_size and tile[1] + 1 < self.grid_size and
                self.tile_map[(tile[0] + 1, tile[1] + 1)]['entity'] == 2):
            self.move_player(tile, (tile[0] + 1, tile[1] + 1))
        elif (tile[0] + 1 < self.grid_size and tile[1] - 1 >= 0 and
                self.tile_map[(tile[0] + 1, tile[1] - 1)]['entity'] == 2):
            self.move_player(tile, (tile[0] + 1, tile[1] - 1))
        elif (tile[0] - 1 >= 0 and tile[1] + 1 < self.grid_size and
                self.tile_map[(tile[0] - 1, tile[1] + 1)]['entity'] == 2):
            self.move_player(tile, (tile[0] - 1, tile[1] + 1))
        elif (tile[0] - 1 >= 0 and tile[1] - 1 >= 0 and
                self.tile_map[(tile[0] - 1, tile[1] - 1)]['entity'] == 2):
            self.move_player(tile, (tile[0] - 1, tile[1] - 1))
        
        print('try_move_player:', tile, 'ent is:', self.tile_map[tile]['entity'])

    def runner(self, event_list, screen):
        self.group_tile.update(event_list, self)
        self.group_tile.draw(screen)

        for ent_id, ent_visual in self.group_ent.items():
            ent_visual.draw(screen)
        
