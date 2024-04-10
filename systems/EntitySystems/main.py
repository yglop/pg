import pygame as pg

from systems.EntitySystems.player_system import PlayerSystem
from systems.EntitySystems.enemy_system import EnemySystem
from systems.EntitySystems.items_system import ItemSystem


class EntityManager():
    def __init__(self):
        self.PS = PlayerSystem() 
        self.ES = EnemySystem()
        self.IS = ItemSystem()
        