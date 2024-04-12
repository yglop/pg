import pygame as pg


class TurnSystem():
    def __init__(self, EM):
        self.EM = EM

    def do_enemy_turn(self):
        for ent_id, ent in self.EM.ent_stats_dict.items():
            if ent_id != 2:
                self.EM.ES.try_move_enemy(ent_id)
                ent.actions = ent.max_actions

    def end_turn(self):
        self.do_enemy_turn()
        self.EM.ent_stats_dict[2].actions = self.EM.ent_stats_dict[2].max_actions
        print('End Turn')
        