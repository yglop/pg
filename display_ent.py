import pygame as pg


class MySprite(pg.sprite.Sprite):
    def __init__(self, tile):
        super().__init__()
        self._layer = 10
        self.image = pg.image.load("./img/player.png")
        self.rect = tile[1]['rect']
        self.rect.center = tile[1]['rect.center']