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
        self.loot_items_buttons = list()

    def open_menu(self):
        self.is_menu_open = True
        self.create_player_items_buttons()

        interactable = self.do_evrything.MS.tile_map[self.do_evrything.EM.mobs_stats[2].tile_id]['interactable']
        if interactable != 0:
            loot_objects = self.do_evrything.EM.interactable_dict[interactable]
            center = [664,234]

            for i in loot_objects:
                loot = InventoryItemButton(center=center, text=i.name)            
                self.loot_items_buttons.append(loot)
                center[1] += 20

    def close_menu(self):
        self.is_menu_open = False
        self.player_items_limbs_buttons.clear()
        self.player_items_organs_buttons.clear()
        self.loot_items_buttons.clear()

    def create_player_items_buttons(self):
        center = [354,234]
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
        center = [204,204]
        ## player limbs
        text = self.font.render(f'Player limbs:', False, (self.text_colour))
        self.do_evrything.screen.blit(text, center)

        for i in self.player_items_limbs_buttons:
            i.update(event_list)
            pg.sprite.RenderPlain(i).draw(self.screen)

            center = i.rect.center

            text = self.font.render(f'{i.text}', False, (self.text_colour))
            self.do_evrything.screen.blit(text, i.rect)
        ## player organs
        text = self.font.render(f'Player organs:', False, (self.text_colour))
        self.do_evrything.screen.blit(text, (center[0]-150, center[1]+14))

        for i in self.player_items_organs_buttons:        
            i.update(event_list)
            pg.sprite.RenderPlain(i).draw(self.screen)

            center = i.rect.center

            text = self.font.render(f'{i.text}', False, (self.text_colour))
            self.do_evrything.screen.blit(text, i.rect)
        ## loot
        text = self.font.render(f'Loot:', False, (self.text_colour))
        self.do_evrything.screen.blit(text, (514,204))

        if len(self.loot_items_buttons) > 0:
            for i in self.loot_items_buttons:
                i.update(event_list)
                pg.sprite.RenderPlain(i).draw(self.screen)

                text = self.font.render(f'{i.text}', False, (self.text_colour))
                self.do_evrything.screen.blit(text, i.rect)
        ## selected item info
        selecred_item = 'Select an item' if True else 'ToDo:Item.name'
        text = self.font.render(f'{selecred_item}:', False, (self.text_colour))
        self.do_evrything.screen.blit(text, (800,204))

        ## inventory
        text = self.font.render(f'Inventory:', False, (self.text_colour))
        self.do_evrything.screen.blit(text, (800,504))


    def draw_menu(self, event_list):
        self.inventory_menu_canvas.update(event_list, self)
        self.inventory_menu_canvas_visual.draw(self.screen)
        