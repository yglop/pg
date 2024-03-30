import pygame as pg


class MySprite(pg.sprite.Sprite):
    def __init__(self, sprite, rect, center):
        super().__init__()
        self._layer = 10
        self.image =  sprite 
        self.rect = rect
        self.rect.center = center