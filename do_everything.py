import pygame as pg
import random

from Visuals.UI.hub import HubMenu
from Visuals.UI.stats_menu import StatsMenu
from Visuals.UI.escape_menu import EscapeMenu
from Visuals.UI.InventoryMenu.inventory_menu import InventoryMenu
from Visuals.UI.popup_window import PopupWindow
from Visuals.UI.hover_window import HoverWindow

from Systems.keyboard_handler import keyboard_handler
from Systems.EntitySystems.entity_manager import EntityManager
from Systems.turn_system import TurnSystem
from Systems.map_system import MapSystem
from Systems.save_manager import SaveManager

class DoEvrything():
    def __init__(self, screen):
        self.screen = screen

        self.MS = None
        self.EM = None
        self.TS = None
        self.stats_menu = None

        self.save_manager = SaveManager()

        self.hub_menu = HubMenu(self.screen)
        self.escape_menu = EscapeMenu(self.screen)
        self.popup_window = PopupWindow(self.screen)
        self.hover_window = HoverWindow(self.screen)

        self.inventory_menu = InventoryMenu(self)

        self.star_the_game(list()) # DEBUG
        
    def star_the_game(self, event_list):
        self.MS = MapSystem()
        self.EM = EntityManager(self.MS, self.save_manager)
        self.TS = TurnSystem(self.EM)

        self.stats_menu = StatsMenu(self)
        event_list.clear()

    def end_the_mission(self, event_list): # BUG! THIS IS SHIT. IT'S LEAKING MEMORY!!!
        self.MS = None
        self.EM = None
        self.TS = None
        self.stats_menu = None
        self.inventory_menu = None

        self.hub_menu.is_open = True
        self.hub_menu.selected_mission = None
        event_list.clear()

    def render_screen(self, event_list):
        self.screen.fill((100,100,100))
        # tiles
        self.MS.group_tile.update(event_list, self)
        self.MS.group_tile.draw(self.screen)
        # entitys
        self.EM.render_ents(self.screen)
        # stats menu
        flag = self.stats_menu.render_all(event_list)
        if flag:
            return
        # popups
        if self.popup_window.is_open:
            self.popup_window.draw_popup()
        # hovers
        if self.hover_window.is_open:
            self.hover_window.draw_hover()

    def runner(self, event_list):
        keyboard_handler(event_list, self)

        ## menus
        if self.escape_menu.is_menu_open:
            self.escape_menu.draw_menu(event_list)
            return      
        if self.hub_menu.is_open:
            flag = self.hub_menu.render_all(event_list)
            if flag:
                self.star_the_game(event_list)
            elif self.inventory_menu.is_menu_open == True:
                pass
            else:
                return 
        if self.inventory_menu.is_menu_open == True:
            self.inventory_menu.render_all(event_list)
            ## popups
            if self.popup_window.is_open == True:
                self.popup_window.draw_popup()
            return

        self.render_screen(event_list)
        
        
