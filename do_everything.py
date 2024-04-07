import pygame as pg
import random

from visuals.display_tile import TileDisplayer
from visuals.display_ent import EntityVisual
from visuals.ui_main import UserInterfaceMain

from map_gen import generate_map

from dataset import tile_sprites_32, player_sprite, enemy_sprite

class DoEvrything():
    def __init__(self):
        self.UI = UserInterfaceMain()
        self.grid_size = 10
        self.group_tile = pg.sprite.RenderPlain()
        self.ent_visual_dict = dict()
        self.tile_map = dict() 
        self.create_tile_map()
        self.create_ent()
        self.create_tiles()

    def create_tile_map(self):
        game_map = generate_map(
            max_rooms=4,
            room_min_size=3,
            room_max_size=3,
            map_width=self.grid_size, 
            map_height=self.grid_size
            )

        tile_image_preset = {
            0: tile_sprites_32[0],
            1: tile_sprites_32[1],
            2: tile_sprites_32[1],
            9: tile_sprites_32[1],
        }
        tile_ent_preset = {
            0: -1,
            1: 2,
            2: 100,
            9: 0,
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
                    'entity': tile_ent,
                }
                
    ##################################### THERE IS A BUG WITH VISUALS OF AN ENAMY
    def create_ent(self):
        ## visuals
        for tile_id, tile_data in self.tile_map.items():
            if tile_data['entity'] == 2:
                new_ent = EntityVisual(player_sprite, tile_data['rect'], tile_data['rect.center'])
                self.ent_visual_dict[tile_data['entity']] = pg.sprite.RenderPlain(new_ent)
            elif tile_data['entity'] not in (0, 2):
                new_ent = EntityVisual(enemy_sprite, tile_data['rect'], tile_data['rect.center'])
                self.ent_visual_dict[tile_data['entity']] = pg.sprite.RenderPlain(new_ent)

    def create_tiles(self):
        for tile_id, tile_data in self.tile_map.items():  
            tile = [tile_id, tile_data]  
            new_tile = TileDisplayer(tile)
            print(tile) #debug
            self.group_tile.add(new_tile)

    def move_player(self, destination_tile, original_tile):
        destination = self.tile_map[destination_tile]
        origin = self.tile_map[original_tile]
        
        if destination['entity'] == 0:
            origin['entity'] = 0
            destination['entity'] = 2

            ent_new_sprite = EntityVisual(player_sprite, destination['rect'], destination['rect.center'])
            self.ent_visual_dict[destination['entity']] = pg.sprite.RenderPlain(ent_new_sprite)

            print('move_player:', 'moved from', original_tile, 'to', destination_tile)
        else:
            print(destination_tile ,'is an enemy tile')

    # dont look at this PLEASE
    def try_move_player(self, tile=(0,0)):
        if self.tile_map[tile]['entity'] == 2:
            print('try_move_player:', tile ,"is player's tile")
        elif self.tile_map[tile]['entity'] == -1:
            print('try_move_player:', tile ,"is impossuble")
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
        # UI
        self.UI.button_manager(event_list, screen, self)

        # tiles
        self.group_tile.update(event_list, self)
        self.group_tile.draw(screen)

        ## tile ent's
        for ent_id, ent_visual in self.ent_visual_dict.items():
            ent_visual.draw(screen)

        
        
