import pygame as pg
from Visuals.display_ent import EntityVisual

def move_mob(
        destination_tile, 
        original_tile, 
        ent_id, 
        tile_map,
        movement_cost,
        ent_stats_dict,
        ent_visual_dict,
        sprite
    ):
    destination = tile_map[destination_tile]
    origin = tile_map[original_tile]
    
    origin['entity'] = 0
    destination['entity'] = ent_id

    ent_stats_dict[ent_id].subtract_action(movement_cost)
    ent_stats_dict[ent_id].tile_id = destination_tile

    ent_new_sprite = EntityVisual(sprite, destination['rect'], destination['rect.center'])
    ent_visual_dict[destination['entity']] = pg.sprite.RenderPlain(ent_new_sprite)
