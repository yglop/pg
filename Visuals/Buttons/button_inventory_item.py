import pygame as pg

from Resources.Textures.dataset import button_inventory_item, button_inventory_item_active, button_inventory_take, button_inventory_drop, button_inventory_equip


class InventoryItemButton(pg.sprite.Sprite):
    def __init__(self, center, data):
        super().__init__()
        self.image = button_inventory_item 
        self.rect = self.image.get_rect()
        self.rect.center = center.copy()

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
                self.change_image()


class InventoryTakeItemButton(pg.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = button_inventory_take 
        self.rect = self.image.get_rect()
        self.rect.center = center.copy()

    def update(self, event_list):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and event.button == 1:
                pass


class InventoryDropItemButton(pg.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = button_inventory_drop 
        self.rect = self.image.get_rect()
        self.rect.center = center.copy()

    def update(self, event_list):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and event.button == 1:
                pass

class InventoryEquipItemButton(pg.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = button_inventory_equip 
        self.rect = self.image.get_rect()
        self.rect.center = center.copy()

    def update(self, event_list):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and event.button == 1:
                pass
        

        