import pygame as pg

from dataset import button_end_turn


class Button(pg.sprite.Sprite):
    def __init__(self, sprite, rect, center):
        super().__init__()
        self.image = sprite 
        self.rect = rect
        self.rect.center = center
        self.clicked = False

    def update(self, event_list):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                self.clicked = not self.clicked
                print('End Turn')


class UserInterfaceMain():
    def __init__(self):
        self.turn_button = Button(button_end_turn, button_end_turn.get_rect(), (1100, 32))
        self.turn_button_visual = pg.sprite.RenderPlain(self.turn_button)

    def button_manager(self, event_list, screen, do_evrything):
        self.turn_button.update(event_list)

        # visuals
        pg.draw.rect(screen, (0,0,100), pg.Rect(1000, 0, 200, 1000))
        self.turn_button_visual.draw(screen)
        