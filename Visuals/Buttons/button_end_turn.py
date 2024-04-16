import pygame as pg

from Resources.Textures.dataset import button_end_turn



class EndTurnButton(pg.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = button_end_turn 
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self, event_list, do_evrything):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                do_evrything.TS.end_turn()
                