import pygame as pg

from Resources.Textures.dataset import inventory_menu

from Visuals.canvas_sprite import CanvasInventory
from Visuals.Buttons.button_inventory_item import InventoryItemButton


class InventoryMenu():
    def __init__(self, do_evrything):
        self.do_evrything = do_evrything
        self.screen = self.do_evrything.screen

        self.inventory_menu_canvas = CanvasInventory(sprite=inventory_menu, center=(600,500))
        self.inventory_menu_canvas_visual = pg.sprite.RenderPlain(self.inventory_menu_canvas)
        
        self.font = pg.font.Font('./Resources/Fonts/consolas.ttf', 13)
        self.text_colour = (160, 160, 255)

        self.is_menu_open = False
        self.player_items_limbs_buttons = list()
        self.player_items_organs_buttons = list()

        self.create_player_items_buttons()

    def open_menu(self):
        self.is_menu_open = True

    def close_menu(self):
        self.is_menu_open = False

    def create_player_items_buttons(self):
        center = [350,230]
        player = self.do_evrything.EM.mobs_stats[2]

        for limb in player.limbs:
            player_item = InventoryItemButton(center=center, text=limb.name)            
            self.player_items_limbs_buttons.append(player_item)
            center[1] += 20

        center[1] += 20

        for organ in player.organs:
            player_item = InventoryItemButton(center=center, text=organ.name)            
            self.player_items_organs_buttons.append(player_item)
            center[1] += 20

    def button_manager(self, event_list):
        center = [200,200]

        text = self.font.render(f'Player limbs:', False, (self.text_colour))
        self.do_evrything.screen.blit(text, center)

        for i in self.player_items_limbs_buttons:
            i.update(event_list)
            pg.sprite.RenderPlain(i).draw(self.screen)

            center = i.rect.center

            text = self.font.render(f'{i.text}', False, (self.text_colour))
            self.do_evrything.screen.blit(text, i.rect)

        text = self.font.render(f'Player organs:', False, (self.text_colour))
        self.do_evrything.screen.blit(text, (center[0]-150, center[1]+10))

        for i in self.player_items_organs_buttons:        
            i.update(event_list)
            pg.sprite.RenderPlain(i).draw(self.screen)

            center = i.rect.center

            text = self.font.render(f'{i.text}', False, (self.text_colour))
            self.do_evrything.screen.blit(text, i.rect)
        
    def draw_menu(self, event_list):
        self.inventory_menu_canvas.update(event_list, self)
        self.inventory_menu_canvas_visual.draw(self.screen)
        