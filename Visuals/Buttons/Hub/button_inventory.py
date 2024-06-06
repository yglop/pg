import pygame as pg

from Resources.Textures.dataset import button_inventory


class HubInventoryButton(pg.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = button_inventory # ToDO
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self, event_list):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos):
                #do_evrything.inventory_menu.open_menu()
                pass # ToDO