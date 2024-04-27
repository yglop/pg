import pygame as pg
import random

from Visuals.UI.stats_menu import StatsMenu
from Visuals.UI.escape_menu import EscapeMenu
from Visuals.UI.InventoryMenu.inventory_menu import InventoryMenu
from Visuals.UI.popup_window import PopupWindow

from Systems.EntitySystems.entity_manager import EntityManager

from Systems.keyboard_handler import keyboard_handler
from Systems.turn_system import TurnSystem
from Systems.map_system import MapSystem

class DoEvrything():
    def __init__(self, screen):
        self.screen = screen

        self.MS = MapSystem()
        self.EM = EntityManager(self.MS)
        self.TS = TurnSystem(self.EM)

        self.stats_menu = StatsMenu(self)
        self.inventory_menu = InventoryMenu(self)
        self.escape_menu = EscapeMenu(self.screen)
        self.popup_window = PopupWindow(self.screen)

    def runner(self, event_list):
        # keyboard
        keyboard_handler(event_list, self)
        
        ## menus
        if self.escape_menu.is_menu_open == True:
            self.escape_menu.draw_menu(event_list)
            return

        if self.inventory_menu.is_menu_open == True:
            self.inventory_menu.render_all(event_list)
            ## popups
            if self.popup_window.is_open == True:
                self.popup_window.draw_popup()
            return

        self.screen.fill((100,100,100))

        self.stats_menu.render_all(event_list)

        # tiles
        self.MS.group_tile.update(event_list, self)
        self.MS.group_tile.draw(self.screen)

        ## tile ent's
        self.EM.render_ents(self.screen)

        ## popups
        if self.popup_window.is_open == True:
            self.popup_window.draw_popup()
        

        
        
