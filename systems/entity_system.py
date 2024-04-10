import pygame as pg

from visuals.display_ent import EntityVisual

from dataset import player_sprite, enemy_sprite


class EntitySystem():
    def __init__(self, tile_map, grid_size, turn_system):
        self.tile_map = tile_map
        self.grid_size = grid_size
        self.turn_system = turn_system
        self.ent_visual_dict = dict()
        self.ent_stats_dict = dict()
        self.iterate_through_tile_map()

    def iterate_through_tile_map(self):
        for tile_id, tile_data in self.tile_map.items():
            if tile_data['entity'] == 2:
                self.append_ent_visual_dict(tile_data, sprite=player_sprite)
                self.append_ent_stats_dict(ent_id=tile_data['entity'])
            elif tile_data['entity'] >= 100:
                self.append_ent_visual_dict(tile_data, sprite=enemy_sprite)
                self.append_ent_stats_dict(ent_id=tile_data['entity'])
    
    def append_ent_visual_dict(self, tile_data, sprite):
        new_ent = EntityVisual(sprite, tile_data['rect'], tile_data['rect.center'])
        self.ent_visual_dict[tile_data['entity']] = pg.sprite.RenderPlain(new_ent)
   
    def append_ent_stats_dict(self, ent_id):
        max_actions = 2
        health = 2
        melee_damage = 1
        self.ent_stats_dict[ent_id] = [max_actions, health, melee_damage]

    def player_melee_attack(self, destination_tile):
        target_ent = self.tile_map[destination_tile]['entity']
        if self.turn_system.current_player_actions > 0:
            self.turn_system.player_did_something(1)
            self.ent_stats_dict[target_ent][1] -= 1
            print('player_melee_attack: player attacks', target_ent)
        if self.ent_stats_dict[target_ent][1] <= 0:
            del self.ent_stats_dict[target_ent]
            del self.ent_visual_dict[target_ent]
            self.tile_map[destination_tile]['entity'] = 0
            print('player_melee_attack:', target_ent, 'died')
        else:
            print('player_melee_attack:', target_ent, 'hp=', self.ent_stats_dict[target_ent][1])

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
            self.player_melee_attack(destination_tile)
            #print('move_player:', destination_tile ,'is an enemy tile')

    def try_move_player(self, tile_id):
        if self.turn_system.is_action_possable() == False:
            print('try_move_player: no actons points left')
            return

        if self.tile_map[tile_id]['entity'] == 2:
            print('try_move_player:', tile_id ,"is player's tile")
            return

        if self.tile_map[tile_id]['entity'] == -1:
            print('try_move_player:', tile_id ,"is impossible")
            return

        for i in self.tile_map[tile_id]['neighbors']:
            if self.tile_map[i]['entity'] == 2:
                self.move_player(tile_id, i)
                return
            
        print('try_move_player: tile', tile_id, 'is unreachable')
    
    def render_ents(self, screen):
        for ent_id, ent_visual in self.ent_visual_dict.items():
            ent_visual.draw(screen)
        