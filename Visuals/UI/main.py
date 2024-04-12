import pygame as pg

from Visuals.Buttons.button_end_turn import EndTurnButton


class UserInterfaceMain():
    def __init__(self, do_evrything):
        self.do_evrything = do_evrything
        self.screen = self.do_evrything.screen

        self.turn_button = EndTurnButton((1100, 52))
        self.turn_button_visual = pg.sprite.RenderPlain(self.turn_button)
        self.font = pg.font.Font(None, 24)

        self.ent_id = None

    def draw_rectangles(self):
        pg.draw.rect(self.screen, (0,0,100), pg.Rect(1000, 0, 200, 1000))
        pg.draw.rect(self.screen, (0,100,100), pg.Rect(1000, 100, 200, 1000))
        pg.draw.rect(self.screen, (0,150,100), pg.Rect(1000, 400, 200, 1000))
        pg.draw.rect(self.screen, (0,200,100), pg.Rect(1000, 700, 200, 1000))

    def render_turn_count(self):
        c_a_p = self.do_evrything.EM.ent_stats_dict[2].actions
        m_a_p = self.do_evrything.EM.ent_stats_dict[2].max_actions
        current_action_points = self.font.render(f'AP left:{c_a_p}/{m_a_p}', False, (0, 180, 0))
        self.screen.blit(current_action_points, (1060, 10))

    def button_manager(self, event_list):
        self.turn_button.update(event_list, self.do_evrything)
        self.turn_button_visual.draw(self.screen)
        
    def render_player_info(self):
        player_hp = self.do_evrything.EM.ent_stats_dict[2].health
        health_text = self.font.render(f'HP:{player_hp}', False, (100, 20, 0))
        self.screen.blit(health_text, (1060, 100))

    def set_enemy_info(self, tile_id):
        if self.do_evrything.MS.tile_map[tile_id]['entity'] >= 100:
            self.ent_id = self.do_evrything.MS.tile_map[tile_id]['entity']

    def render_enemy_info(self):
        if self.ent_id in self.do_evrything.EM.ent_stats_dict:
            enemy_hp = self.do_evrything.EM.ent_stats_dict[self.ent_id].health
            health_text = self.font.render(f'HP:{enemy_hp}', False, (100, 20, 0))
            self.screen.blit(health_text, (1060, 400))

    def render_logs(self):
        pass

