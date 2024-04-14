import pygame as pg
import random

from Visuals.UI.main import UserInterfaceMain
from Visuals.UI.escape_menu import EscapeMenu

from Systems.EntitySystems.main import EntityManager

from Systems.keyboard_handler import keyboard_handler
from Systems.turn_system import TurnSystem
from Systems.map_system import MapSystem

class DoEvrything():
    def __init__(self, screen):
        self.screen = screen

        self.MS = MapSystem()
        self.EM = EntityManager(self.MS)
        self.TS = TurnSystem(self.EM)
        self.UI = UserInterfaceMain(self)
        self.escape_menu = EscapeMenu(self.screen)

    def runner(self, event_list):
        # keyboard
        keyboard_handler(event_list, self)
        
        if self.escape_menu.is_menu_open == True:
            self.escape_menu.draw_menu(event_list)
            return

        self.screen.fill((100,100,100))

        # UI
        self.UI.render_all(event_list)

        # tiles
        self.MS.group_tile.update(event_list, self)
        self.MS.group_tile.draw(self.screen)

        ## tile ent's
        self.EM.render_ents(self.screen)
        

        
        
