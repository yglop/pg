import pygame as pg

from Resources.Textures.dataset import button_mission


class HubMissionButton(pg.sprite.Sprite):
    def __init__(self, center, text):
        super().__init__()
        self.image = button_mission 
        self.rect = self.image.get_rect()
        self.rect.center = center

        self.text = text
        self.text_center = (self.rect.center[0]-144, self.rect.center[1]-10)

    def update(self, event_list):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos):
                pass # ToDO