import pygame as pg


class PopupWindow():
    def __init__(self, screen):
        self.screen = screen

        self.font = pg.font.Font('./Resources/Fonts/consolas.ttf', 26)
        self.text_colour = (160, 160, 255)

        self.text = str()
        self.is_open = False

    def open_popup(self, text):
        self.text = text
        self.is_open = True

    def close_popup(self):
        self.text = ''
        self.is_open = False

    def draw_popup(self):
        window = pg.Rect(300, 100, 600, 100)
        pg.draw.rect(self.screen, (35,45,45), window)

        text = self.font.render(f'{self.text}', False, (self.text_colour))
        self.screen.blit(text, (320, 150))