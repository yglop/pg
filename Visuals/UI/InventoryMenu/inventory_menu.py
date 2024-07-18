import pygame as pg

from Visuals.UI.InventoryMenu.create_buttons import CreateButtons
from Visuals.UI.InventoryMenu.render_items import RenderItems
from Visuals.UI.InventoryMenu.interaction_buttons import InteractionButtons

from Systems.EntitySystems.Entity.mob import Mob


class InventoryMenu():
    def __init__(self, do_evrything):
        self.do_evrything = do_evrything
        self.screen = self.do_evrything.screen
        self.player = None

        self.is_menu_open = False
        self.buttons = None
        self.interaction_buttons = None
        self.render_items = None

        self.selecred_item = None
        self.is_hub_open = self.do_evrything.hub_menu.is_open

    def get_player(self):
        if self.is_hub_open == True:
            self.do_evrything.save_manager.load_save()
            self.player = Mob(self.do_evrything.save_manager.player) # BUG it will breake the game 
        else:
            self.player = self.do_evrything.EM.mobs_stats[2]

    def open_menu(self):
        self.is_menu_open = True
        self.get_player()
        self.buttons = CreateButtons(self.do_evrything, self.player)
        self.interaction_buttons = InteractionButtons(self)
        self.render_items = RenderItems(self)

    def close_menu(self):
        self.is_menu_open = False
        self.selecred_item = None
        self.buttons.player_limbs_buttons.empty()
        self.buttons.player_organs_buttons.empty()
        self.buttons.player_armour_button.empty()
        self.buttons.player_in_hands_buttons.empty()
        self.buttons.player_storage_buttons.empty()
        self.buttons.loot_buttons.empty()
        #self.buttons.interaction_buttons.empty()
        self.render_items.inventory_menu_canvas_visual.empty()
        del self.buttons
        del self.render_items
        if self.is_hub_open == False:
            self.do_evrything.stats_menu.create_weapon_buttons()

    def reopen_menu(self, event_list):
        self.player.update_stats()
        self.close_menu()
        self.do_evrything.stats_menu.render_all(event_list)
        self.open_menu()

    def unselect_items(self):
        for i in (
            self.buttons.player_limbs_buttons.sprites() +
            self.buttons.player_organs_buttons.sprites() +
            self.buttons.player_armour_button.sprites() +
            self.buttons.player_in_hands_buttons.sprites() +
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
            self.buttons.player_in_hands_buttons.sprites() +
            self.buttons.player_storage_buttons.sprites() +
            self.buttons.loot_buttons.sprites() 
            ):
            if i.selected and self.is_hub_open == False:
                self.interaction_buttons.create_interaction_buttons()
                return
        self.selecred_item = None
        self.interaction_buttons.interaction_buttons.empty()

    def check_if_open(self):
        if self.is_menu_open:
            return
        self.close_menu()

    def render_all(self, event_list):
        self.render_items.render(event_list)

        self.check_for_selected_item()
        self.check_if_open()
        