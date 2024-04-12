import pygame as pg
import random

from visuals.ui.main import UserInterfaceMain

from systems.EntitySystems.main import EntityManager

from systems.keyboard_handler import keyboard_handler
from systems.turn_system import TurnSystem
from systems.map_system import MapSystem

class DoEvrything():
    def __init__(self, screen):
        self.screen = screen

        self.MS = MapSystem()
        self.EM = EntityManager(self.MS)
        self.TS = TurnSystem(self.EM)
        self.UI = UserInterfaceMain(self)

    def runner(self, event_list):
        # UI
        self.UI.draw_rectangles()
        self.UI.button_manager(event_list)
        self.UI.render_turn_count()
        self.UI.render_player_info()
        self.UI.render_enemy_info()

        # tiles
        self.MS.group_tile.update(event_list, self)
        self.MS.group_tile.draw(self.screen)

        ## tile ent's
        self.EM.render_ents(self.screen)

        # keyboard
        keyboard_handler(event_list, self)

        
        
