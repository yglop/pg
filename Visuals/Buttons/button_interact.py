import pygame as pg

from Resources.Textures.dataset import button_interact



class InteractButton(pg.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = button_interact 
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.clicked = False

    def update(self, event_list, do_evrything):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                self.clicked = not self.clicked
                pass