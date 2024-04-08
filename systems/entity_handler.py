import pygame as pg

from visuals.display_ent import EntityVisual

from dataset import player_sprite, enemy_sprite


class EntityHandler():
    def __init__(self, tile_map, grid_size, turn_system):
        self.tile_map = tile_map
        self.grid_size = grid_size
        self.turn_system = turn_system
        self.ent_visual_dict = dict()
        self.create_ent_visual_dict()
    
    def create_ent_visual_dict(self):
        for tile_id, tile_data in self.tile_map.items():
            if tile_data['entity'] == 2:
                new_ent = EntityVisual(player_sprite, tile_data['rect'], tile_data['rect.center'])
                self.ent_visual_dict[tile_data['entity']] = pg.sprite.RenderPlain(new_ent)
            elif tile_data['entity'] not in (0, 2, -1):
                new_ent = EntityVisual(enemy_sprite, tile_data['rect'], tile_data['rect.center'])
                self.ent_visual_dict[tile_data['entity']] = pg.sprite.RenderPlain(new_ent)
   
    def move_player(self, destination_tile, original_tile):
        destination = self.tile_map[destination_tile]
        origin = self.tile_map[original_tile]
        
        if destination['entity'] == 0:
            origin['entity'] = 0
            destination['entity'] = 2

            ent_new_sprite = EntityVisual(player_sprite, destination['rect'], destination['rect.center'])
            self.ent_visual_dict[destination['entity']] = pg.sprite.RenderPlain(ent_new_sprite)

            self.turn_system.player_did_something(1)
            print('move_player:', 'moved from', original_tile, 'to', destination_tile)
        else:
            print(destination_tile ,'is an enemy tile')

    # dont look at this PLEASE
    def try_move_player(self, tile):
        if self.turn_system.is_action_possable() == False:
            print('try_move_player: no actons points left')
        elif self.tile_map[tile]['entity'] == 2:
            print('try_move_player:', tile ,"is player's tile")
        elif self.tile_map[tile]['entity'] == -1:
            print('try_move_player:', tile ,"is impossible")
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

    def render_ents(self, screen):
        for ent_id, ent_visual in self.ent_visual_dict.items():
            ent_visual.draw(screen)
        