import pygame as pg

from Resources.Textures.dataset import (
    button_inventory_item, button_inventory_item_active, 
    button_inventory_take, button_inventory_drop, 
    button_inventory_equip, button_inventory_eat
    )


class InventoryItemButton(pg.sprite.Sprite):
    def __init__(self, center, data):
        super().__init__()
        self.image = button_inventory_item 
        self.rect = self.image.get_rect()
        self.rect.center = center.copy()

        self.font = pg.font.Font('./Resources/Fonts/consolas.ttf', 13)
        self.text_colour = (160, 160, 255)

        self.data = data
        self.selected = False

    def select(self):
        self.image = button_inventory_item_active
        self.selected = True

    def unselect(self):
        self.image = button_inventory_item
        self.selected = False

    def change_image(self, IM):
        if self.selected == False:
            self.select()
            IM.selecred_item = self
            IM.unselect_items()
        else:
            self.unselect()

    def update(self, IM, event_list):
        IM.render_items.render_button_text(self.data.name, self.rect.center)
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and event.button == 1:
                self.change_image(IM)

'''
class InventoryTakeItemButton(pg.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = button_inventory_take 
        self.rect = self.image.get_rect()
        self.rect.center = center.copy()

    def update(self, event_list, do_evrything):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and event.button == 1:
                do_evrything.inventory_menu.take_item()
                do_evrything.inventory_menu.reopen_menu(event_list)


class InventoryDropItemButton(pg.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = button_inventory_drop 
        self.rect = self.image.get_rect()
        self.rect.center = center.copy()

    def update(self, event_list, do_evrything):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and event.button == 1:
                do_evrything.inventory_menu.drop_item()
                do_evrything.inventory_menu.reopen_menu(event_list)


class InventoryEquipItemButton(pg.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = button_inventory_equip 
        self.rect = self.image.get_rect()
        self.rect.center = center.copy()

    def update(self, event_list, do_evrything):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and event.button == 1:
                do_evrything.inventory_menu.equip_item()
                do_evrything.inventory_menu.reopen_menu(event_list)


class InventoryEatItemButton(pg.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = button_inventory_eat 
        self.rect = self.image.get_rect()
        self.rect.center = center.copy()

    def update(self, event_list, do_evrything):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and event.button == 1:
                do_evrything.inventory_menu.eat_item()
                do_evrything.inventory_menu.reopen_menu(event_list)
'''