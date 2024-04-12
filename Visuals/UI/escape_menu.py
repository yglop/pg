import pygame as pg

from Resources.Textures.dataset import in_game_menu
from Visuals.canvas_sprite import CanvasSprite

class EscapeMenu():
    def __init__(self, screen):
        self.screen = screen
        self.game_menu_visual = pg.sprite.RenderPlain(CanvasSprite(sprite=in_game_menu, center=(400,400)))
        self.is_menu_open = False

    def open_menu(self):
        self.is_menu_open = True

    def close_menu(self):
        self.is_menu_open = False

    def draw_menu(self):
        self.game_menu_visual.draw(self.screen)
