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
        pg.image.load("./Resources/Textures/tiles/ss/wall.png"), 
        pg.image.load("./Resources/Textures/tiles/ss/floor1.png"), 
        pg.image.load("./Resources/Textures/tiles/ss/floor.png"), 
        pg.image.load("./Resources/Textures/tiles/x32/tile-yellow.png"),
    )


# Ent
player_sprite = pg.image.load("./Resources/Textures/ent/player.png")
enemy_sprite = pg.image.load("./Resources/Textures/ent/enemy.png")



# UI
button_end_turn = pg.image.load("./Resources/Textures/UI/button-EndTurn.png")
button_close_game = pg.image.load("./Resources/Textures/UI/button-CloseGame.png")

button_inventory = pg.image.load("./Resources/Textures/UI/button-Inventory.png")
button_inventory_active = pg.image.load("./Resources/Textures/UI/button-InventoryActive.png")

button_inventory_item = pg.image.load("./Resources/Textures/UI/inventory_buttons/button-InventoryItem.png")
button_inventory_item_active = pg.image.load("./Resources/Textures/UI/inventory_buttons/button-InventoryItemActive.png")
button_inventory_interaction = pg.image.load("./Resources/Textures/UI/inventory_buttons/button-InventoryInteracton.png")

button_mission = pg.image.load("./Resources/Textures/UI/button_mission.png")

in_game_menu = pg.image.load("./Resources/Textures/UI/in_game_menu.png")
inventory_menu = pg.image.load("./Resources/Textures/UI/inventory_menu.png")

## weapons
weapon_base = pg.image.load("./Resources/Textures/UI/weapon_buttons/weapon-base.png")
weapon_base_active = pg.image.load("./Resources/Textures/UI/weapon_buttons/weapon-base-active.png")
