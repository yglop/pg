import pygame as pg


class CanvasSprite(pg.sprite.Sprite):
    def __init__(self, sprite, center):
        super().__init__()
        self.image = sprite 
        self.rect = self.image.get_rect()
        self.rect.center = center


class CanvasInventory(pg.sprite.Sprite):
    def __init__(self, sprite, center):
        super().__init__()
        self.image = sprite 
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self, event_list, RI):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and not self.rect.collidepoint(event.pos):
                RI.IM.is_menu_open = False