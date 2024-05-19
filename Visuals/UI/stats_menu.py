import pygame as pg

from Visuals.Buttons.button_end_turn import EndTurnButton
from Visuals.Buttons.button_inventory import InventoryButton
from Visuals.Buttons.weapon_buttons import WeaponButtonBase


class StatsMenu():
    def __init__(self, do_evrything):
        self.do_evrything = do_evrything
        self.player = self.do_evrything.EM.mobs_stats[2]
        self.screen = self.do_evrything.screen

        self.turn_button = EndTurnButton((1100, 52))
        self.turn_button_visual = pg.sprite.RenderPlain(self.turn_button)

        self.inventory_button = InventoryButton((1170, 52))
        self.inventory_button_visual = pg.sprite.RenderPlain(self.inventory_button)

        self.weapon_buttons = pg.sprite.RenderPlain()
        self.create_weapon_buttons()

        self.font = pg.font.Font('./Resources/Fonts/arial_bold.ttf', 16)
        self.text_colour = (30, 30, 30)

        self.mob_id = None

    def set_enemy_info(self, tile_id):
        if self.do_evrything.MS.tile_map[tile_id]['mob'] >= 100:
            self.mob_id = self.do_evrything.MS.tile_map[tile_id]['mob']

    def create_weapon_buttons(self):
        center = [1016, 140]
        self.weapon_buttons.empty()
        for i in self.player.in_hands:
            weapon_btn = WeaponButtonBase(center=center, data=i)            
            self.weapon_buttons.add(weapon_btn)
            center[0] += 32
            if len(self.weapon_buttons.sprites()) % 6 == 0:
                center[0] -= 192
                center[1] += 32

    ## renders
    def draw_rectangles(self):
        pg.draw.rect(self.screen, (0,0,100), pg.Rect(1000, 0, 200, 1000))
        pg.draw.rect(self.screen, (0,100,100), pg.Rect(1000, 100, 200, 1000))
        pg.draw.rect(self.screen, (0,150,100), pg.Rect(1000, 400, 200, 1000))
        pg.draw.rect(self.screen, (0,200,100), pg.Rect(1000, 700, 200, 1000))

    def render_AP_MP_count(self):
        c_a_p = self.player.actions
        m_a_p = self.player.max_actions
        c_m_p = self.player.movements
        m_m_p = self.player.max_movements
        
        current_action_points = self.font.render(f'AP:{c_a_p}/{m_a_p} MP:{c_m_p}/{m_m_p}', False, (0, 180, 0))
        self.screen.blit(current_action_points, (1050, 10))

    def render_turn_button(self, event_list):
        self.turn_button.update(event_list, self.do_evrything)
        self.turn_button_visual.draw(self.screen)

    def render_loot_button(self, event_list):
        loot = self.do_evrything.MS.tile_map[self.player.tile_id]['loot']
        if (loot != 0) and (len(self.do_evrything.EM.interactable_dict[loot]) > 0):
            self.inventory_button.change_image(True)
        else:
            self.inventory_button.change_image(False)
        self.inventory_button.update(event_list, self.do_evrything)
        self.inventory_button_visual.draw(self.screen)

    def render_weapon_buttons(self, event_list):
        self.weapon_buttons.update(event_list)
        self.weapon_buttons.draw(self.screen)
        
    def render_player_info(self):
        player = self.player
        text = self.font.render(f'nutrition: {player.nutrition}/{player.max_nutrition}', False, (self.text_colour))
        self.screen.blit(text, (1000,100))    
    
    def render_enemy_info(self):
        if self.mob_id in self.do_evrything.EM.mobs_stats:
            self.render_mob_info(self.mob_id, [1000,400])

    def render_mob_info(self, mob_id, pos):
        mob_name = self.do_evrything.EM.mobs_stats[mob_id].name
        mob_limbs = self.do_evrything.EM.mobs_stats[mob_id].limbs
        mob_organs = self.do_evrything.EM.mobs_stats[mob_id].organs

        text_hight = 18
        
        name_text = self.font.render(f'{mob_name}', False, (self.text_colour))
        self.screen.blit(name_text, pos)
        pos[1] += text_hight

        self.screen.blit(self.font.render(f'  LIMBS:', False, (self.text_colour)), pos)       
        pos[1] += text_hight

        for i in mob_limbs:
            limb_stat_text = self.font.render(f'{i.name}: {i.health}', False, (self.text_colour))
            self.screen.blit(limb_stat_text, pos)
            pos[1] += text_hight
        
        self.screen.blit(self.font.render(f'  ORGANS:', False, (self.text_colour)), pos)
        pos[1] += text_hight

        for i in mob_organs:
            organ_stat_text = self.font.render(f'{i.name}: {i.health}', False, (self.text_colour))
            self.screen.blit(organ_stat_text, pos)
            pos[1] += text_hight

    def render_logs(self):
        pass

    def render_all(self, event_list):
        self.draw_rectangles()
        self.render_turn_button(event_list)
        self.render_loot_button(event_list)
        self.render_weapon_buttons(event_list)
        self.render_AP_MP_count()
        self.render_player_info()
        self.render_enemy_info()
