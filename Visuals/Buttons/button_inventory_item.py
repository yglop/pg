import pygame as pg

from Resources.Textures.dataset import button_inventory_item, button_inventory_item_active


class InventoryItemButton(pg.sprite.Sprite):
    def __init__(self, center, data):
        super().__init__()
        self.image = button_inventory_item 
        self.rect = self.image.get_rect()
        self.rect.center = center.copy()
        self.clicked = False

        self.data = data
        self.selected = False

    def change_image(self):
        if self.image == button_inventory_item:
            self.image = button_inventory_item_active
            self.selected = True
        else:
            self.image = button_inventory_item
            self.selected = False

    def update(self, event_list):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and event.button == 1:
                self.clicked = not self.clicked
                self.change_image()


        


        

        