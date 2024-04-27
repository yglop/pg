import pygame as pg

from Visuals.Buttons.button_inventory_item import InventoryItemButton


class CreateButtons():
    def __init__(self, player):
        self.player = player

        self.player_limbs_buttons = pg.sprite.RenderPlain()
        self.player_organs_buttons = pg.sprite.RenderPlain()

        self.player_armour_button = pg.sprite.RenderPlain()
        self.player_storage_buttons = pg.sprite.RenderPlain()

        self.loot_objects = None
        self.loot_buttons = pg.sprite.RenderPlain()

        self.interaction_buttons = pg.sprite.RenderPlain()

        self.create_first_column_buttons()
        self.create_second_column_buttons()

    def create_first_column_buttons(self):
        center = [304,228]

        for i in self.player.limbs:
            player_item = InventoryItemButton(center=center, data=i)            
            self.player_limbs_buttons.add(player_item)
            center[1] += 16

        center[1] += 16

        for i in self.player.organs:
            player_item = InventoryItemButton(center=center, data=i)            
            self.player_organs_buttons.add(player_item)
            center[1] += 16

    def create_second_column_buttons(self):
        center = [514,212]
        if self.player.armour:
            player_item = InventoryItemButton(center=center, data=self.player.armour)
            self.player_armour_button.add(player_item)
            center[1] += 16
        center[1] += 16
        for i in self.player.storage:
            player_item = InventoryItemButton(center=center, data=i)
            self.player_storage_buttons.add(player_item)
            center[1] += 16

    def create_loot_buttons(self):
        if self.loot_objects:
            pass

