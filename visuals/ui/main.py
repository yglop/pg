import pygame as pg

from visuals.ui.end_turn_button import EndTurnButton
from dataset import button_end_turn


class UserInterfaceMain():
    def __init__(self):
        self.turn_button = EndTurnButton(button_end_turn, button_end_turn.get_rect(), (1100, 52))
        self.turn_button_visual = pg.sprite.RenderPlain(self.turn_button)
        self.font = pg.font.Font(None, 24)

    def render_turn_count(self, screen, do_evrything):
        c_a_p = do_evrything.TS.current_player_actions
        m_a_p = do_evrything.TS.max_player_actions
        current_action_points = self.font.render(f'AP left:{c_a_p}/{m_a_p}', False, (0, 180, 0))
        screen.blit(current_action_points, (1060, 10))

    def button_manager(self, event_list, screen, do_evrything):
        self.turn_button.update(event_list, do_evrything)

        # visuals
        pg.draw.rect(screen, (0,0,100), pg.Rect(1000, 0, 200, 1000))
        self.turn_button_visual.draw(screen)
        