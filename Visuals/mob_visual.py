import pygame as pg


class MobVisual(pg.sprite.Sprite):
    def __init__(self, sprite, rect, center):
        super().__init__()
        self.image = sprite 
        self.rect = rect
        self.rect.center = center