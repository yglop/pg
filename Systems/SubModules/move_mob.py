import pygame as pg


def move_mob(
        destination_tile, 
        original_tile, 
        ent_id, 
        tile_map,
        movement_cost,
        mobs_stats,
        sprite
    ):
    destination = tile_map[destination_tile]
    origin = tile_map[original_tile]
    
    origin['mob'] = 0
    destination['mob'] = ent_id

    mobs_stats[ent_id].subtract_movement(movement_cost)
    mobs_stats[ent_id].tile_id = destination_tile
