import pygame as pg


class HoverWindow():
    def __init__(self, screen):
        self.screen = screen

        self.font = pg.font.Font('./Resources/Fonts/consolas.ttf', 16)
        self.text_colour = (160, 160, 255)

        self.text = str()
        self.pos = None
        self.is_open = False

    def open_hover(self, text, pos):
        self.text = text
        self.pos = (pos[0]-120, pos[1]-30)
        self.is_open = True

    def close_hover(self):
        self.text = ''
        self.is_open = False

    def draw_hover(self):
        window = pg.Rect(self.pos[0]-2, self.pos[1]-1, len(self.text)*10, 20)
        pg.draw.rect(self.screen, (35,45,45), window)

        text = self.font.render(f'{self.text}', False, (self.text_colour))
        self.screen.blit(text, self.pos)