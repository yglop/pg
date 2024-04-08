import pygame as pg


class TurnSystem():
    def __init__(self):
        self.max_player_actions = int()
        self.current_player_actions = int()

    def get_max_player_actions(self, max_player_actions=1):
        self.max_player_actions = max_player_actions
        self.current_player_actions = max_player_actions

    def player_did_something(self, action_cost=1):
        self.current_player_actions -= action_cost

    def is_action_possable(self, action_cost=1):
        return self.current_player_actions >= action_cost

    def end_turn(self):
        self.current_player_actions = self.max_player_actions