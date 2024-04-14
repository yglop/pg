import pygame as pg

from Visuals.Buttons.button_end_turn import EndTurnButton
from Visuals.Buttons.button_interact import InteractButton

class UserInterfaceMain():
    def __init__(self, do_evrything):
        self.do_evrything = do_evrything
        self.screen = self.do_evrything.screen

        self.turn_button = EndTurnButton((1100, 52))
        self.turn_button_visual = pg.sprite.RenderPlain(self.turn_button)

        self.intecat_button = InteractButton((1170, 52))
        self.intecat_button_visual = pg.sprite.RenderPlain(self.intecat_button)

        self.font = pg.font.Font(None, 24)

        self.ent_id = None

    def draw_rectangles(self):
        pg.draw.rect(self.screen, (0,0,100), pg.Rect(1000, 0, 200, 1000))
        pg.draw.rect(self.screen, (0,100,100), pg.Rect(1000, 100, 200, 1000))
        pg.draw.rect(self.screen, (0,150,100), pg.Rect(1000, 400, 200, 1000))
        pg.draw.rect(self.screen, (0,200,100), pg.Rect(1000, 700, 200, 1000))

    def render_turn_count(self):
        c_a_p = self.do_evrything.EM.mobs_stats[2].actions
        m_a_p = self.do_evrything.EM.mobs_stats[2].max_actions
        current_action_points = self.font.render(f'AP left:{c_a_p}/{m_a_p}', False, (0, 180, 0))
        self.screen.blit(current_action_points, (1060, 10))

    def button_manager(self, event_list):
        self.turn_button.update(event_list, self.do_evrything)
        self.turn_button_visual.draw(self.screen)

        if self.do_evrything.MS.tile_map[self.do_evrything.EM.mobs_stats[2].tile_id]['interactable'] != 0:
            self.intecat_button.update(event_list, self.do_evrything)
            self.intecat_button_visual.draw(self.screen)
        
    def render_player_info(self):
        pass
        #player_hp = self.do_evrything.EM.mobs_stats[2].health
        #health_text = self.font.render(f'HP:{player_hp}', False, (100, 20, 0))
        #self.screen.blit(health_text, (1000, 100))

    def set_enemy_info(self, tile_id):
        if self.do_evrything.MS.tile_map[tile_id]['mob'] >= 100:
            self.ent_id = self.do_evrything.MS.tile_map[tile_id]['mob']

    def render_enemy_info(self):
        if self.ent_id in self.do_evrything.EM.mobs_stats:
            enemy_name = self.do_evrything.EM.mobs_stats[self.ent_id].name
            enemy_limbs = self.do_evrything.EM.mobs_stats[self.ent_id].limbs
            enemy_organs = self.do_evrything.EM.mobs_stats[self.ent_id].organs
            
            health_text = self.font.render(f'{enemy_name}', False, (100, 20, 0))
            self.screen.blit(health_text, (1000, 400))

            limb_stat_display = [1000, 420]
            for i in enemy_limbs:
                limb_stat_text = self.font.render(f'{i.name}: {i.health}', False, (100, 20, 0))
                self.screen.blit(limb_stat_text, limb_stat_display)
                limb_stat_display[1] += 20
            
            self.screen.blit(self.font.render(f'', False, (100, 20, 0)), limb_stat_display)
            limb_stat_display[1] += 20

            for i in enemy_organs:
                organ_stat_text = self.font.render(f'{i.name}: {i.health}', False, (100, 20, 0))
                self.screen.blit(organ_stat_text, limb_stat_display)
                limb_stat_display[1] += 20


    def render_logs(self):
        pass

