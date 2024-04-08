import pygame as pg
import random

from visuals.display_tile import TileVisual
from visuals.ui.main import UserInterfaceMain

from mapgen.map_gen import generate_map
from systems.entity_handler import EntityHandler
from systems.turn_system import TurnSystem

from dataset import tile_sprites_32

class DoEvrything():
    def __init__(self):
        self.UI = UserInterfaceMain()
        self.TS = TurnSystem()
        self.grid_size = 30
        self.group_tile = pg.sprite.RenderPlain()
        self.tile_map = dict() 

        self.create_tile_map()
        self.create_tiles()

        self.ent_handler = EntityHandler(self.tile_map, self.grid_size, self.TS)
        self.TS.get_max_player_actions(max_player_actions=2)

    def create_tile_map(self):
        game_map = generate_map(
            max_rooms=12,
            room_min_size=3,
            room_max_size=12,
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

    def runner(self, event_list, screen):
        # UI
        self.UI.button_manager(event_list, screen, self)
        self.UI.render_turn_count(screen, self)

        # tiles
        self.group_tile.update(event_list, self)
        self.group_tile.draw(screen)

        ## tile ent's
        self.ent_handler.render_ents(screen)

        
        
