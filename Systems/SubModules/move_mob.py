import pygame as pg
from Visuals.display_ent import EntityVisual

def move_mob(
        destination_tile, 
        original_tile, 
        ent_id, 
        tile_map,
        movement_cost,
        mobs_stats,
        mobs_visual,
        sprite
    ):
    destination = tile_map[destination_tile]
    origin = tile_map[original_tile]
    
    origin['mob'] = 0
    destination['mob'] = ent_id

    mobs_stats[ent_id].subtract_action(movement_cost)
    mobs_stats[ent_id].tile_id = destination_tile

    ent_new_sprite = EntityVisual(sprite, destination['rect'], destination['rect.center'])
    mobs_visual[destination['mob']] = pg.sprite.RenderPlain(ent_new_sprite)
