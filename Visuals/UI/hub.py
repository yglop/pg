import pygame as pg


class HubMenu():
    def __init__(self, screen):
        self.screen = screen

        self.is_open = False
        self.reputation = [0, 0, 0, 0]

    def render_all(self):
        self.screen.fill((0,100,100))
