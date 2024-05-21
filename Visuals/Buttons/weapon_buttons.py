import pygame as pg

from Resources.Textures.dataset import weapon_base, weapon_base_active


class WeaponButtonBase(pg.sprite.Sprite):
    def __init__(self, center, data):
        super().__init__()
        self.image = weapon_base 
        self.rect = self.image.get_rect()
        self.rect.center = center

        self.data = data
        self.selected = False

    def select(self):
        self.image = weapon_base_active
        self.selected = True

    def unselect(self):
        self.image = weapon_base
        self.selected = False

    def update(self, event_list, SM):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos):
                if self.selected == False:
                    self.select()
                    SM.player.selected_weapon = self.data
                    SM.unselect_weapons()
                else:
                    self.unselect()
                    SM.player.selected_weapon = None
            if self.rect.collidepoint(pg.mouse.get_pos()):
                damage = None
                if hasattr(self.data, 'melee_damage'):
                    damage = self.data.melee_damage
                elif hasattr(self.data, 'range_damage'):
                    damage = self.data.range_damage
                    
                SM.do_evrything.hover_window.open_hover(f'{self.data.name} damage:{damage}', self.rect.center)
            else:
                SM.do_evrything.hover_window.close_hover()

        
                