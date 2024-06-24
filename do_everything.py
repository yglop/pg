import pygame as pg
import random

from Visuals.UI.stats_menu import StatsMenu
from Visuals.UI.InventoryMenu.inventory_menu import InventoryMenu
from Visuals.UI.popup_window import PopupWindow
from Visuals.UI.hover_window import HoverWindow

from Systems.EntitySystems.entity_manager import EntityManager
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
        self.popup_window = PopupWindow(self.screen)
        self.hover_window = HoverWindow(self.screen)

    '''
    def _init(self):
        self.MS = MapSystem()
        self.EM = EntityManager(self.MS)
        self.TS = TurnSystem(self.EM)

        self.stats_menu = StatsMenu(self)
        self.inventory_menu = InventoryMenu(self)
        self.popup_window = PopupWindow(self.screen)
        self.hover_window = HoverWindow(self.screen)
        print('hui')
    '''

    def render_screen(self, event_list):
        self.screen.fill((100,100,100))
        # tiles
        self.MS.group_tile.update(event_list, self)
        self.MS.group_tile.draw(self.screen)
        # entitys
        self.EM.render_ents(self.screen)
        # left menu
        self.stats_menu.render_all(event_list)
        # popups
        if self.popup_window.is_open:
            self.popup_window.draw_popup()
        # hovers
        if self.hover_window.is_open:
            self.hover_window.draw_hover()

    def runner(self, event_list):
        ## menus
        if self.inventory_menu.is_menu_open == True:
            self.inventory_menu.render_all(event_list)
            ## popups
            if self.popup_window.is_open == True:
                self.popup_window.draw_popup()
            return

        self.render_screen(event_list)
        
        
