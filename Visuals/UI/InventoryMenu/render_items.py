import pygame as pg

from Resources.Textures.dataset import inventory_menu

from Visuals.canvas_sprite import CanvasInventory


class RenderItems():
    def __init__(self, IM):
        self.IM = IM
        self.screen = IM.screen
        self.player = IM.player

        self.inventory_menu_canvas = CanvasInventory(sprite=inventory_menu, center=(600,500))
        self.inventory_menu_canvas_visual = pg.sprite.RenderPlain(self.inventory_menu_canvas)

        self.font = pg.font.Font('./Resources/Fonts/consolas.ttf', 13)
        self.text_colour = (160, 160, 255)

    def render_canvas(self, event_list):
        self.inventory_menu_canvas.update(event_list, self)
        self.inventory_menu_canvas_visual.draw(self.screen)

    def render_text(self, txt, pos):
        text = self.font.render(txt, False, (self.text_colour))
        self.screen.blit(text, pos)

    def render_buttons(self, _buttons, event_list):
        _buttons.draw(self.screen)
        _buttons.update(self.IM, event_list)

    def render_button_text(self, name, pos):
        text = self.font.render(f'{name}', False, (self.text_colour))
        self.screen.blit(text, (pos[0]-100, pos[1]-7))

    def render_first_column(self, event_list):
        # player limbs
        self.render_text(f'limb points: {self.player.used_limb_points}/{self.player.max_limb_points}', (204,204))
        self.render_buttons(self.IM.buttons.player_limbs_buttons, event_list)
        # player organs
        self.render_text(
            f'organ points: {self.player.used_organ_points}/{self.player.max_organ_points}', 
            (204, self.IM.buttons.player_organs_buttons.sprites()[0].rect.center[1] - 23))
        self.render_buttons(self.IM.buttons.player_organs_buttons, event_list)

    def render_second_column(self, event_list):
        storage_pos1 = 204
        # armour
        if self.IM.buttons.player_armour_button:
            self.render_buttons(self.IM.buttons.player_armour_button, event_list)
            storage_pos1 = 220
        # storage
        self.render_text(
            f'Storage capacity: {self.player.storage_capacity}/{self.player.max_storage_capacity}', 
            (414, storage_pos1))
        self.render_buttons(self.IM.buttons.player_storage_buttons, event_list)

    def render_loot_items(self, event_list):
        self.render_text(f'Loot:', (796,504))
        self.render_buttons(self.IM.buttons.loot_buttons, event_list)

    def render_setected_item_info(self):
        text = self.IM.selecred_item.data.name if self.IM.selecred_item else 'Select an item'
        self.render_text(f'{text}', (796,204))
        
        if self.IM.selecred_item:
            center = [796,240]
            ### i know this is bs, but this bs works
            if hasattr(self.IM.selecred_item.data, 'weight'):
                self.render_text(f'weight: {self.IM.selecred_item.data.weight}', center)
                center[1] += 16
            if hasattr(self.IM.selecred_item.data, 'health'):
                self.render_text(f'health: {self.IM.selecred_item.data.health}/{self.IM.selecred_item.data.max_health}', center)
                center[1] += 16
            if hasattr(self.IM.selecred_item.data, 'nutrition'):
                self.render_text(f'nutrition: {self.IM.selecred_item.data.nutrition}', center)
                center[1] += 16
            if hasattr(self.IM.selecred_item.data, 'limb_points'):
                self.render_text(f'limb points: {self.IM.selecred_item.data.limb_points}', center)
                center[1] += 16
            if hasattr(self.IM.selecred_item.data, 'action_points'):
                self.render_text(f'action points: {self.IM.selecred_item.data.action_points}', center)
                center[1] += 16
            if hasattr(self.IM.selecred_item.data, 'melee_damage'):
                self.render_text(f'melee damage: {self.IM.selecred_item.data.melee_damage}', center)
                center[1] += 16
            if hasattr(self.IM.selecred_item.data, 'organ_points'):
                self.render_text(f'organ points: {self.IM.selecred_item.data.organ_points}', center)
                center[1] += 16 
            if hasattr(self.IM.selecred_item.data, 'critical'):
                self.render_text(f'critical: {self.IM.selecred_item.data.critical}', center)
                center[1] += 16
            if hasattr(self.IM.selecred_item.data, 'protection'):
                self.render_text(f'protection: {self.IM.selecred_item.data.protection}', center)
                center[1] += 16

    def render(self, event_list):
        self.render_canvas(event_list)
        self.render_first_column(event_list)
        self.render_second_column(event_list)
        self.render_loot_items(event_list)

        self.render_setected_item_info()