import pygame as pg

from Resources.Textures.dataset import button_inventory_item, button_inventory_item_active


class InventoryItemButton(pg.sprite.Sprite):
    def __init__(self, center, text):
        super().__init__()
        self.image = button_inventory_item 
        self.rect = self.image.get_rect()
        self.rect.center = center.copy()
        self.clicked = False

        self.text = text

    def change_image(self):
        if self.image == button_inventory_item:
            self.image = button_inventory_item_active
        else:
            self.image = button_inventory_item

    def update(self, event_list):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                self.clicked = not self.clicked
                self.change_image()


        


        

        