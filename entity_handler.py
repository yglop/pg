import pygame as pg

from visuals.display_ent import EntityVisual

from dataset import player_sprite, enemy_sprite


class EntityHandler():
    def __init__(self, tile_map):
        self.tile_map = tile_map
        self.ent_visual_dict = dict()
    '''
    for tile_id, tile_data in self.tile_map.items():
            if tile_data['entity'] == 2:
                new_ent = EntityVisual(player_sprite, tile_data['rect'], tile_data['rect.center'])
                self.ent_visual_dict[tile_data['entity']] = pg.sprite.RenderPlain(new_ent)
            elif tile_data['entity'] not in (0, 2, -1):
                new_ent = EntityVisual(enemy_sprite, tile_data['rect'], tile_data['rect.center'])
                self.ent_visual_dict[tile_data['entity']] = pg.sprite.RenderPlain(new_ent)

    def render_ents(self):
        for ent_id, ent_visual in self.ent_visual_dict.items():
            ent_visual.draw(screen)
    '''