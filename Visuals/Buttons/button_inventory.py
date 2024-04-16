import pygame as pg

from Resources.Textures.dataset import button_inventory, button_inventory_active



class InventoryButton(pg.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = button_inventory 
        self.rect = self.image.get_rect()
        self.rect.center = center

    def change_image(self, active):
        if active:
            self.image = button_inventory_active
        else:
            self.image = button_inventory

    def update(self, event_list, do_evrything):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                do_evrything.inventory_menu.open_menu()