import pygame as pg

from Visuals.Buttons.button_inventory_item import InteractionButton


class InteractionButtons():
    def __init__(self, IM):
        self.IM = IM

        self.interaction_buttons = pg.sprite.RenderPlain()

    def create_interaction_button(self, center, state):
        btn = InteractionButton(center=center, state=state)   
        self.interaction_buttons.add(btn)

    def create_interaction_buttons(self):
        center = [816,228]
        if (self.IM.selecred_item.data in (self.IM.player.limbs + self.IM.player.organs)) or (self.IM.selecred_item.data is self.IM.player.armour):
            self.interaction_buttons.empty()

            self.create_interaction_button(center, 'take') 
            center[0] += 40
            self.create_interaction_button(center, 'drop')     
            center[0] += 40
        elif self.IM.selecred_item.data in self.IM.player.storage:
            self.interaction_buttons.empty()

            self.create_interaction_button(center, 'drop')
            center[0] += 40
            self.create_interaction_button(center, 'equip')  
            center[0] += 40

            if hasattr(self.IM.selecred_item.data, 'nutrition'):
                self.create_interaction_button(center, 'eat')
        elif self.IM.buttons.loot_objects and (self.IM.selecred_item.data in (self.IM.buttons.loot_objects)):
            self.interaction_buttons.empty()
            
            self.create_interaction_button(center, 'take') 
            center[0] += 40
            self.create_interaction_button(center, 'equip') 
            center[0] += 40   

            if hasattr(self.IM.selecred_item.data, 'nutrition'):
                self.create_interaction_button(center, 'eat')   

    def interact_with_item(self, state):
        state_dict = {
            'take':self.take_item(),
            'drop':self.drop_item(),
            'equip':self.equip_item(),
            'eat':self.eat_item()
        }
        state_dict[state]
    #################################################################### REWRITE THIS BS
    def take_item(self):
        if self.IM.selecred_item.data.weight + self.IM.player.storage_capacity > self.IM.player.max_storage_capacity:
            print('take_item: storage has no space')
            self.IM.do_evrything.popup_window.open_popup('storage has no space')
            return

        if self.IM.selecred_item.data in self.IM.player.limbs and (self.IM.selecred_item.data.nutrition + 100 < self.IM.player.nutrition):
            self.IM.player.storage.append(self.IM.selecred_item.data)
            self.IM.player.limbs.remove(self.IM.selecred_item.data)
            self.IM.player.nutrition -= self.IM.selecred_item.data.nutrition + 100
        elif self.IM.selecred_item.data in self.IM.player.organs and (self.IM.selecred_item.data.nutrition + 100 < self.IM.player.nutrition):
            self.IM.player.storage.append(self.IM.selecred_item.data)
            self.IM.player.organs.remove(self.IM.selecred_item.data)
            self.IM.player.nutrition -= self.IM.selecred_item.data.nutrition + 100
        elif self.IM.selecred_item.data is self.IM.player.armour:
            self.IM.player.storage.append(self.IM.selecred_item.data)
            self.IM.player.armour = None
        elif self.IM.buttons.loot_objects and (self.IM.selecred_item.data in self.IM.buttons.loot_objects):
            self.IM.player.storage.append(self.IM.selecred_item.data)
            self.IM.buttons.loot_objects.remove(self.IM.selecred_item.data)

    def drop_item(self):
        if hasattr(self.IM.selecred_item.data, 'nutrition') and ((self.IM.selecred_item.data.nutrition + 100 > self.IM.player.nutrition) 
            and not (self.IM.selecred_item.data in self.IM.player.storage)):
            print('drop_item: nutrition is too low')
            self.IM.do_evrything.popup_window.open_popup('nutrition is too low')
            return

        if self.IM.buttons.loot_objects:
            self.IM.buttons.loot_objects += [self.IM.selecred_item.data,]
        else:
            entity_manager = self.IM.do_evrything.EM
            self.IM.do_evrything.MS.tile_map[self.IM.player.tile_id]['loot'] = self.IM.do_evrything.EM.interactable_id_count
            entity_manager.interactable_dict[entity_manager.interactable_id_count] = [self.IM.selecred_item.data,]
            entity_manager.interactable_id_count += 1

        if self.IM.selecred_item.data in self.IM.player.limbs:
            self.IM.player.limbs.remove(self.IM.selecred_item.data)
            self.IM.player.nutrition -= self.IM.selecred_item.data.nutrition + 100
        elif self.IM.selecred_item.data in self.IM.player.organs:
            self.IM.player.organs.remove(self.IM.selecred_item.data)
            self.IM.player.nutrition -= self.IM.selecred_item.data.nutrition + 100
        elif self.IM.selecred_item.data in self.IM.player.storage:
            self.IM.player.storage.remove(self.IM.selecred_item.data)
        elif self.IM.selecred_item.data is self.IM.player.armour:
            self.IM.player.armour = None

    def equip_item(self):
        if hasattr(self.IM.selecred_item.data, 'nutrition') and (self.IM.selecred_item.data.nutrition + 50 > self.IM.player.nutrition):
            print('equip_item: nutrition is too low') 
            self.IM.do_evrything.popup_window.open_popup('nutrition is too low')
            return

        if self.IM.selecred_item.data in self.IM.player.storage:
            if hasattr(self.IM.selecred_item.data, 'limb_points'):
                self.IM.player.limbs.append(self.IM.selecred_item.data)
                self.IM.player.storage.remove(self.IM.selecred_item.data)
            elif hasattr(self.IM.selecred_item.data, 'organ_points'):
                self.IM.player.organs.append(self.IM.selecred_item.data)
                self.IM.player.storage.remove(self.IM.selecred_item.data)
            elif hasattr(self.IM.selecred_item.data, 'protection'):
                self.IM.player.armour = self.IM.selecred_item.data
                self.IM.player.storage.remove(self.IM.selecred_item.data)
        elif self.IM.buttons.loot_objects and (self.IM.selecred_item.data in self.IM.buttons.loot_objects):
            if hasattr(self.IM.selecred_item.data, 'limb_points'):
                self.IM.player.limbs.append(self.IM.selecred_item.data)
                self.IM.buttons.loot_objects.remove(self.IM.selecred_item.data)
            elif hasattr(self.IM.selecred_item.data, 'organ_points'):
                self.IM.player.organs.append(self.IM.selecred_item.data)
                self.IM.buttons.loot_objects.remove(self.IM.selecred_item.data)
            elif hasattr(self.IM.selecred_item.data, 'protection'):
                self.IM.player.armour = self.IM.selecred_item.data
                self.IM.buttons.loot_objects.remove(self.IM.selecred_item.data)

        if hasattr(self.IM.selecred_item.data, 'nutrition'):
            self.IM.player.nutrition -= self.IM.selecred_item.data.nutrition + 50

    def eat_item(self):
        self.IM.player.nutrition += self.IM.selecred_item.data.nutrition
        if self.IM.selecred_item.data in self.IM.player.storage:
            self.IM.player.storage.remove(self.IM.selecred_item.data)
        elif self.IM.buttons.loot_objects and (self.IM.selecred_item.data in self.IM.buttons.loot_objects):
            self.IM.buttons.loot_objects.remove(self.IM.selecred_item.data)

    