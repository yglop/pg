import pygame as pg

from Resources.Textures.dataset import button_inventory_item, button_inventory_item_active, button_inventory_interaction


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
        IM.render_items.render_button_text(self.data.name, (self.rect.center[0]-100, self.rect.center[1]-7))
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and event.button == 1:
                self.change_image(IM)


class InteractionButton(pg.sprite.Sprite):
    def __init__(self, center, state):
        super().__init__()
        self.image = button_inventory_interaction
        self.rect = self.image.get_rect()
        self.rect.center = center.copy()

        self.state = state

    def update(self, IM, event_list):
        IM.render_items.render_button_text(self.state, (self.rect.center[0]-16, self.rect.center[1]-7))
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and event.button == 1:
                IM.interaction_buttons.interact_with_item(self.state)
                IM.reopen_menu(event_list)
