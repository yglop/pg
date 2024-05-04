import pygame as pg


class TurnSystem():
    def __init__(self, EM):
        self.EM = EM

    def do_enemy_turn(self):
        for ent_id, ent in self.EM.mobs_stats.items():
            if ent_id != 2:
                self.EM.ES.try_move_enemy(ent_id)
                ent.actions = ent.max_actions
                ent.movements = ent.max_movements

    def end_turn(self):
        self.do_enemy_turn()
        self.EM.mobs_stats[2].actions = self.EM.mobs_stats[2].max_actions
        self.EM.mobs_stats[2].movements = self.EM.mobs_stats[2].max_movements
        print('End Turn')
        