import pygame as pg

from Resources.Textures.dataset import inventory_menu

from Visuals.canvas_sprite import CanvasInventory


class InventoryMenu():
    def __init__(self, screen):
        self.screen = screen

        self.inventory_menu_canvas = CanvasInventory(sprite=inventory_menu, center=(550,450))
        self.inventory_menu_canvas_visual = pg.sprite.RenderPlain(self.inventory_menu_canvas)
        
        self.is_menu_open = False

    def open_menu(self):
        self.is_menu_open = True

    def close_menu(self):
        self.is_menu_open = False

    def draw_menu(self, event_list):
        self.inventory_menu_canvas.update(event_list, self)
        self.inventory_menu_canvas_visual.draw(self.screen)