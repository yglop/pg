import pygame as pg


# Tiles
tile_sprites_64 = (
        pg.image.load("./Resources/Textures/tiles/x32/tile-empty.png"), 
        pg.image.load("./Resources/Textures/tiles/x64/tile-blue.png"), 
        pg.image.load("./Resources/Textures/tiles/x64/tile-green.png"), 
        pg.image.load("./Resources/Textures/tiles/x64/tile-red.png"), 
        pg.image.load("./Resources/Textures/tiles/x64/tile-yellow.png"),
    )

tile_sprites_32 = (
        pg.image.load("./Resources/Textures/tiles/x32/tile-empty.png"), 
        pg.image.load("./Resources/Textures/tiles/x32/tile-blue.png"), 
        pg.image.load("./Resources/Textures/tiles/x32/tile-green.png"), 
        pg.image.load("./Resources/Textures/tiles/x32/tile-red.png"), 
        pg.image.load("./Resources/Textures/tiles/x32/tile-yellow.png"),
    )


# Ent
player_sprite = pg.image.load("./Resources/Textures/ent/player.png")
enemy_sprite = pg.image.load("./Resources/Textures/ent/enemy.png")



# UI
button_end_turn = pg.image.load("./Resources/Textures/UI/button-EndTurn.png")