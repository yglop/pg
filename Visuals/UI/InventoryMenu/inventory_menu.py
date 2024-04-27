import pygame as pg

from Visuals.UI.InventoryMenu.create_buttons import CreateButtons
from Visuals.UI.InventoryMenu.render_items import RenderItems


class InventoryMenu():
    def __init__(self, do_evrything):
        self.do_evrything = do_evrything
        self.screen = self.do_evrything.screen
        self.player = self.do_evrything.EM.mobs_stats[2]

        self.is_menu_open = False
        self.buttons = None
        self.render_items = None

        self.selecred_item = None

    def open_menu(self):
        self.is_menu_open = True
        self.buttons = CreateButtons(self.do_evrything, self.player)
        self.render_items = RenderItems(self)

    def close_menu(self):
        self.is_menu_open = False

    def unselect_items(self):
        for i in (
            self.buttons.player_limbs_buttons.sprites() +
            self.buttons.player_organs_buttons.sprites() +
            self.buttons.player_armour_button.sprites() +
            self.buttons.player_storage_buttons.sprites() +
            self.buttons.loot_buttons.sprites() 
            ):
            if i is not self.selecred_item:
                i.unselect()

    def check_for_selected_item(self):
        for i in (
            self.buttons.player_limbs_buttons.sprites() +
            self.buttons.player_organs_buttons.sprites() +
            self.buttons.player_armour_button.sprites() +
            self.buttons.player_storage_buttons.sprites() +
            self.buttons.loot_buttons.sprites() 
            ):
            if i.selected:
                return
        self.selecred_item = None

    def render_all(self, event_list):
        self.render_items.render(event_list)

        self.check_for_selected_item()
        