import pygame as pg


class CanvasSprite(pg.sprite.Sprite):
    def __init__(self, sprite, center):
        super().__init__()
        self.image = sprite 
        self.rect = self.image.get_rect()
        self.rect.center = center