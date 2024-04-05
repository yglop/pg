import pygame as pg


class Button(pg.sprite.Sprite):
    def __init__(self, image, rect, center):
        super().__init__()
        self.image = image 
        self.rect = rect
        self.rect.center = center
        self.clicked = False

    def update(self, event_list):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                self.clicked = not self.clicked


class UserInterfaceMain():
    def __init__(self):
        pass