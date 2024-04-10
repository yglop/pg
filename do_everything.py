import pygame as pg
import random

from visuals.ui.main import UserInterfaceMain

from systems.entity_system import EntitySystem
from systems.keyboard_handler import keyboard_handler
from systems.turn_system import TurnSystem
from systems.map_system import MapSystem

class DoEvrything():
    def __init__(self):
        self.UI = UserInterfaceMain()
        self.TS = TurnSystem()
        self.MS = MapSystem()

        self.ES = EntitySystem(self.MS.tile_map, self.MS.grid_size, self.TS)
        self.TS.get_max_player_actions(self.ES.ent_stats_dict[2][0])


    def runner(self, event_list, screen):
        # UI
        self.UI.button_manager(event_list, screen, self)
        self.UI.render_turn_count(screen, self)

        # tiles
        self.MS.group_tile.update(event_list, self)
        self.MS.group_tile.draw(screen)

        ## tile ent's
        self.ES.render_ents(screen)

        # keyboard
        keyboard_handler(event_list, self)

        
        
