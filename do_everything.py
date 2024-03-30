import pygame as pg
import random

from display_tile import TileDisplayer
from display_ent import EntityVisual
from dataset import *

class DoEvrything():
    def __init__(self):
        self.grid_size = 5
        self.group_tile = pg.sprite.RenderPlain()
        self.ent_visual_dict = dict()
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
        enemy_count = 3
        while enemy_count >= 0:
            tile_ids = list(self.tile_map.keys())
            choicen_tile = random.choice(tile_ids)
            if self.tile_map[choicen_tile]['entity'] == 0:
                self.tile_map[choicen_tile]['entity'] = 100 + enemy_count
                enemy_count -= 1

        ## visuals
        for tile_id, tile_data in self.tile_map.items():
            if tile_data['entity'] == 2:
                new_ent = EntityVisual(player_sprite, tile_data['rect'], tile_data['rect.center'])
                self.ent_visual_dict[tile_data['entity']] = pg.sprite.RenderPlain(new_ent)
            elif tile_data['entity'] != 0 and tile_data['entity'] != 2:
                new_ent = EntityVisual(enemy_sprite, tile_data['rect'], tile_data['rect.center'])
                self.ent_visual_dict[tile_data['entity']] = pg.sprite.RenderPlain(new_ent)

    def create_tiles(self):
        for tile_id, tile_data in self.tile_map.items():  
            tile = [tile_id, tile_data]  
            new_tile = TileDisplayer(tile)

            self.group_tile.add(new_tile)

    def move_player(self, destination_tile, original_tile):
        destination = self.tile_map[destination_tile]
        origin = self.tile_map[original_tile]
        
        if destination['entity'] != 1:
            origin['entity'] = 0
            destination['entity'] = 2

            ent_new_sprite = EntityVisual(player_sprite, destination['rect'], destination['rect.center'])
            self.ent_visual_dict[destination['entity']] = pg.sprite.RenderPlain(ent_new_sprite)

            print('move_player:', 'moved from', original_tile, 'to', destination_tile)
        else:
            print(destination_tile ,'is enamy tile')

    # dont look at this PLEASE
    def try_move_player(self, tile=(0,0)):
        if self.tile_map[tile]['entity'] == 2:
            print('try_move_player:', tile ,"is player's tile")
        elif (tile[0] + 1 < self.grid_size and 
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
        else:
            print('try_move_player: tile', tile, 'is unreachable')

    def runner(self, event_list, screen):
        self.group_tile.update(event_list, self)
        self.group_tile.draw(screen)

        for ent_id, ent_visual in self.ent_visual_dict.items():
            ent_visual.draw(screen)
        
