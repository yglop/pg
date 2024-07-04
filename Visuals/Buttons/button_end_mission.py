import pygame as pg

from Resources.Textures.dataset import button_inventory # ToDo: unique sprite



class EndMissionButton(pg.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = button_inventory 
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self, event_list, do_evrything):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and event.button == 1:
                do_evrything.end_the_mission(event_list)
                return True
                