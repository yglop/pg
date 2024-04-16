import pygame as pg

from Resources.Textures.dataset import inventory_menu

from Visuals.canvas_sprite import CanvasInventory
from Visuals.Buttons.button_inventory_item import InventoryItemButton, InventoryTakeItemButton, InventoryDropItemButton, InventoryEquipItemButton


class InventoryMenu():
    def __init__(self, do_evrything):
        self.do_evrything = do_evrything
        self.screen = self.do_evrything.screen

        self.inventory_menu_canvas = CanvasInventory(sprite=inventory_menu, center=(600,500))
        self.inventory_menu_canvas_visual = pg.sprite.RenderPlain(self.inventory_menu_canvas)
        
        self.font = pg.font.Font('./Resources/Fonts/consolas.ttf', 13)
        self.text_colour = (160, 160, 255)

        self.is_menu_open = False

        self.player = self.do_evrything.EM.mobs_stats[2]
        self.loot_objects = None
        self.selecred_item = None

        self.player_items_limbs_buttons = list()
        self.player_items_organs_buttons = list()
        self.player_items_storage_buttons = list()
        self.loot_items_buttons = list()

        self.interaction_buttons = list()

    def open_menu(self):
        self.is_menu_open = True
        self.create_player_items_buttons()

        tile_interactable = self.do_evrything.MS.tile_map[self.player.tile_id]['interactable']
        if tile_interactable != 0:
            self.loot_objects = self.do_evrything.EM.interactable_dict[tile_interactable]
            center = [514,226]

            for i in self.loot_objects:
                loot = InventoryItemButton(center=center, data=i)            
                self.loot_items_buttons.append(loot)
                center[1] += 16

    def close_menu(self):
        self.is_menu_open = False
        self.player_items_limbs_buttons.clear()
        self.player_items_organs_buttons.clear()
        self.player_items_storage_buttons.clear()
        self.loot_items_buttons.clear()
        self.interaction_buttons.clear()
        self.selecred_item = None

    def create_player_items_buttons(self):
        center = [304,226]

        for i in self.player.limbs:
            player_item = InventoryItemButton(center=center, data=i)            
            self.player_items_limbs_buttons.append(player_item)
            center[1] += 16

        center[1] += 16

        for i in self.player.organs:
            player_item = InventoryItemButton(center=center, data=i)            
            self.player_items_organs_buttons.append(player_item)
            center[1] += 16

        center = [800,520]
        for i in self.player.storage:
            player_item = InventoryItemButton(center=center, data=i)
            self.player_items_storage_buttons.append(player_item)
            center[1] += 16

    def create_interaction_buttons(self):
        if self.selecred_item:
            center = [820,228]
            if self.selecred_item.data in (self.player.limbs + self.player.organs):
                self.interaction_buttons.clear()

                btn_take = InventoryTakeItemButton(center=center)   
                self.interaction_buttons.append(btn_take)  
                center[0] += 40

                btn_drop = InventoryDropItemButton(center=center)  
                self.interaction_buttons.append(btn_drop)  
            elif self.selecred_item.data in (self.loot_objects):
                self.interaction_buttons.clear()
                
                btn_take = InventoryTakeItemButton(center=center)   
                self.interaction_buttons.append(btn_take)  
                center[0] += 40

                btn_equip = InventoryEquipItemButton(center=center)   
                self.interaction_buttons.append(btn_equip)  
                center[0] += 40       
            elif self.selecred_item in self.player.storage:
                self.interaction_buttons.clear()

                btn_drop = InventoryDropItemButton(center=center)   
                self.interaction_buttons.append(btn_drop)  
                center[0] += 40

                btn_equip = InventoryEquipItemButton(center=center)   
                self.interaction_buttons.append(btn_equip)  
                center[0] += 40  
            if False:
                self.close_menu()
                self.open_menu()

    def unselect_items(self, item):
        for i in (
            self.player_items_limbs_buttons + 
            self.player_items_organs_buttons + 
            self.loot_items_buttons
            ):
            if i != item and i.selected:
                i.change_image()

    def check_for_selected_item(self):
        for i in (
            self.player_items_limbs_buttons + 
            self.player_items_organs_buttons + 
            self.player_items_storage_buttons +
            self.loot_items_buttons
            ):
            if i.selected:
                return
        self.selecred_item = None
        self.interaction_buttons.clear()

    def render_player_items_buttons(self, event_list):
        center = [204,204]
        self.player = self.do_evrything.EM.mobs_stats[2]
        ## player limbs
        text = self.font.render(f'limb points: {self.player.used_limb_points}/{self.player.max_limb_points}', False, (self.text_colour))
        self.do_evrything.screen.blit(text, center)

        for i in self.player_items_limbs_buttons:
            i.update(event_list)
            pg.sprite.RenderPlain(i).draw(self.screen)

            if i.selected:
                self.selecred_item = i
                self.unselect_items(i)

            center = i.rect.center

            text = self.font.render(f'{i.data.name}', False, (self.text_colour))
            self.do_evrything.screen.blit(text, (i.rect[0]+2, i.rect[1]+1))
        ## player organs
        text = self.font.render(f'organ points: {self.player.used_organ_points}/{self.player.max_organ_points}', False, (self.text_colour))
        self.do_evrything.screen.blit(text, (center[0]-100, center[1]+10))

        for i in self.player_items_organs_buttons:        
            i.update(event_list)
            pg.sprite.RenderPlain(i).draw(self.screen)

            if i.selected:
                self.selecred_item = i
                self.unselect_items(i)

            center = i.rect.center

            text = self.font.render(f'{i.data.name}', False, (self.text_colour))
            self.do_evrything.screen.blit(text, (i.rect[0]+2, i.rect[1]+1))

    def render_loot_buttons(self, event_list):
        text = self.font.render(f'Loot:', False, (self.text_colour))
        self.do_evrything.screen.blit(text, (414,204))

        if len(self.loot_items_buttons) > 0:
            for i in self.loot_items_buttons:
                i.update(event_list)
                pg.sprite.RenderPlain(i).draw(self.screen)

                if i.selected:
                    self.selecred_item = i
                    self.unselect_items(i)

                text = self.font.render(f'{i.data.name}', False, (self.text_colour))
                self.do_evrything.screen.blit(text, (i.rect[0]+2, i.rect[1]+1))

    def render_setected_item_info(self):
        selecred_item = self.selecred_item.data.name if self.selecred_item else 'Select an item'
        text = self.font.render(f'{selecred_item}', False, (self.text_colour))
        self.do_evrything.screen.blit(text, (800,204))
        
        if self.selecred_item:
            center = [800,240]
            ### YES, IT SHOUL LOOCK LIKE THAT. NO ITS NOT POSSUBLE TO JUST ALLOCATE ALL THIS SHIT TO ANOTHER FUNCTION. I TRIED AND I FAILED.
            text = self.font.render(f'weight: {self.selecred_item.data.weight}', False, (self.text_colour))
            self.do_evrything.screen.blit(text, center)
            center[1] += 16
            text = self.font.render(f'health: {self.selecred_item.data.health}', False, (self.text_colour))
            self.do_evrything.screen.blit(text, center)
            center[1] += 16
            if hasattr(self.selecred_item.data, 'limb_points'):
                text = self.font.render(f'limb points: {self.selecred_item.data.limb_points}', False, (self.text_colour))
                self.do_evrything.screen.blit(text, center)
                center[1] += 16
            if hasattr(self.selecred_item.data, 'action_points'):
                text = self.font.render(f'action points: {self.selecred_item.data.action_points}', False, (self.text_colour))
                self.do_evrything.screen.blit(text, center)
                center[1] += 16
            if hasattr(self.selecred_item.data, 'melee_damage'):
                text = self.font.render(f'melee damage: {self.selecred_item.data.melee_damage}', False, (self.text_colour))
                self.do_evrything.screen.blit(text, center)
                center[1] += 16
            if hasattr(self.selecred_item.data, 'critical'):
                text = self.font.render(f'critical: {self.selecred_item.data.critical}', False, (self.text_colour))
                self.do_evrything.screen.blit(text, center)
                center[1] += 16
            if hasattr(self.selecred_item.data, 'organ_points'):
                text = self.font.render(f'organ points: {self.selecred_item.data.organ_points}', False, (self.text_colour))
                self.do_evrything.screen.blit(text, center)
                center[1] += 16 
            if hasattr(self.selecred_item.data, 'protection'):
                text = self.font.render(f'protection: {self.selecred_item.data.protection}', False, (self.text_colour))
                self.do_evrything.screen.blit(text, center)
                center[1] += 16

    def render_inventory_buttons(self, event_list):
        text = self.font.render(f'Inventory:', False, (self.text_colour))
        self.do_evrything.screen.blit(text, (800,504))

        for i in self.player_items_storage_buttons:        
            i.update(event_list)
            pg.sprite.RenderPlain(i).draw(self.screen)

            if i.selected:
                self.selecred_item = i
                self.unselect_items(i)

            text = self.font.render(f'{i.data.name}', False, (self.text_colour))
            self.do_evrything.screen.blit(text, (i.rect[0]+2, i.rect[1]+1))

    def render_interaction_buttons(self, event_list):
        for i in self.interaction_buttons:
            i.update(event_list)
            pg.sprite.RenderPlain(i).draw(self.screen)

    def draw_menu(self, event_list):
        self.inventory_menu_canvas.update(event_list, self)
        self.inventory_menu_canvas_visual.draw(self.screen)
        
    def render_all(self, event_list):
        self.draw_menu(event_list)

        self.render_player_items_buttons(event_list)
        self.render_loot_buttons(event_list)
        self.render_inventory_buttons(event_list)
        self.render_interaction_buttons(event_list)

        self.render_setected_item_info()

        self.check_for_selected_item()
        self.create_interaction_buttons()