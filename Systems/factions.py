import pygame as pg

from Systems.mission import Mission

class Factions():
    def __init__(self):
        self.reputation = [0, 1, 2, 3]
        self.missions0 = [Mission(), Mission()]
        self.missions1 = [Mission(), Mission()]
        self.missions2 = [Mission(), Mission()]
        self.missions3 = [Mission(), Mission()]