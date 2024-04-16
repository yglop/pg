import pygame as pg

from Resources.Textures.dataset import button_close_game


class CloseGameButton(pg.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = button_close_game 
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self, event_list):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and event.button == 1:
                pg.quit()