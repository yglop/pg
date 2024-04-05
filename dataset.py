import pygame as pg


# Tiles
tile_sprites = (
        pg.image.load("./img/tile-blue.png"), 
        pg.image.load("./img/tile-green.png"), 
        pg.image.load("./img/tile-red.png"), 
        pg.image.load("./img/tile-yellow.png"),
    )



# Ent
player_sprite = pg.image.load("./img/player.png")
enemy_sprite = pg.image.load("./img/enemy.png")



# UI
button_end_turn = pg.image.load("./img/button-EndTurn.png")