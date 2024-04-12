import pygame as pg

from Resources.Textures.dataset import in_game_menu

from Visuals.canvas_sprite import CanvasSprite
from Visuals.Buttons.button_close_game import CloseGameButton


class EscapeMenu():
    def __init__(self, screen):
        self.screen = screen

        self.game_menu_visual = pg.sprite.RenderPlain(CanvasSprite(sprite=in_game_menu, center=(500,400)))

        self.close_game_button = CloseGameButton((500,570))
        self.close_game_button_visual = pg.sprite.RenderPlain(self.close_game_button)

        self.is_menu_open = False

    def open_menu(self):
        self.is_menu_open = True

    def close_menu(self):
        self.is_menu_open = False

    def draw_menu(self, event_list):
        self.game_menu_visual.draw(self.screen)
        self.close_game_button.update(event_list)
        self.close_game_button_visual.draw(self.screen)
