import pygame as pg


class EndTurnButton(pg.sprite.Sprite):
    def __init__(self, sprite, rect, center):
        super().__init__()
        self.image = sprite 
        self.rect = rect
        self.rect.center = center
        self.clicked = False

    def update(self, event_list, do_evrything):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                self.clicked = not self.clicked
                do_evrything.TS.end_turn()
                