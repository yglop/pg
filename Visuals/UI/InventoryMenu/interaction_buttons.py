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
        self.interaction_buttons.empty()
        btns_kwords = list()
        kword = str()
        ## kword0
        if self.IM.selecred_item.data in self.IM.player.limbs:
            btns_kwords = ['take', 'drop']
            kword = 'limb'
        elif self.IM.selecred_item.data in self.IM.player.organs:
            btns_kwords = ['take', 'drop']
            kword = 'organ'
        elif self.IM.selecred_item.data is self.IM.player.armour: 
            btns_kwords = ['take', 'drop']
            kword = 'armour'
        elif self.IM.buttons.loot_objects and (self.IM.selecred_item.data in (self.IM.buttons.loot_objects)):
            btns_kwords = ['take', 'equip']
            if hasattr(self.IM.selecred_item.data, 'nutrition'):
                btns_kwords.append('eat')
            kword = 'loot'
        elif self.IM.selecred_item.data in self.IM.player.storage:
            btns_kwords = ['drop', 'equip']
            if hasattr(self.IM.selecred_item.data, 'nutrition'):
                btns_kwords.append('eat')
            kword = 'storage'

        center = [816,228]
        for i in btns_kwords:
            self.create_interaction_button(center, (i, kword))
            center[0] += 40

    ## interactions
    def interact_with_item(self, state):
        if state[0] == 'take':
            self.take_item(state)
        elif state[0] == 'drop':
            self.drop_item(state)
        elif state[0] == 'equip':
            self.equip_item(state),
        elif state[0] == 'eat':
            self.eat_item(state)

    def take_item(self, state):
        # storage has capacity for item
        if self.IM.selecred_item.data.weight + self.IM.player.storage_capacity > self.IM.player.max_storage_capacity:
            print('take_item: storage has no space')
            self.IM.do_evrything.popup_window.open_popup('storage has no space')
            return
        # item is armour OR item in loot
        if state[1] == 'armour':
            self.IM.player.storage.append(self.IM.selecred_item.data)
            self.IM.player.armour = None
            return
        elif state[1] == 'loot':
            self.IM.player.storage.append(self.IM.selecred_item.data)
            self.IM.buttons.loot_objects.remove(self.IM.selecred_item.data)

        # item in limbs or organs
        if self.IM.selecred_item.data.nutrition + 100 > self.IM.player.nutrition:
            print('take_item: nutrition is too low')
            self.IM.do_evrything.popup_window.open_popup('nutrition is too low')
            return
        else:
            self.IM.player.nutrition -= self.IM.selecred_item.data.nutrition + 100
            self.IM.player.storage.append(self.IM.selecred_item.data)
            if state[1] == 'limb' :
                self.IM.player.limbs.remove(self.IM.selecred_item.data)
            elif state[1] == 'organ':
                self.IM.player.organs.remove(self.IM.selecred_item.data)
            return

    def create_loot(self):
        if self.IM.buttons.loot_objects:
            self.IM.buttons.loot_objects += [self.IM.selecred_item.data,]
        else:
            entity_manager = self.IM.do_evrything.EM
            self.IM.do_evrything.MS.tile_map[self.IM.player.tile_id]['loot'] = self.IM.do_evrything.EM.interactable_id_count
            entity_manager.interactable_dict[entity_manager.interactable_id_count] = [self.IM.selecred_item.data,]
            entity_manager.interactable_id_count += 1

    def drop_item(self, state):
        #item is armour OR item in storage
        if state[1] == 'armour':
            self.create_loot()
            self.IM.player.armour = None
            return
        elif state[1] == 'storage':
            self.create_loot()
            self.IM.player.storage.remove(self.IM.selecred_item.data)
            return
        # player has enough nutrition
        if hasattr(self.IM.selecred_item.data, 'nutrition') and (self.IM.selecred_item.data.nutrition + 100 > self.IM.player.nutrition):
            print('drop_item: nutrition is too low')
            self.IM.do_evrything.popup_window.open_popup('nutrition is too low')
            return
        self.create_loot()
        self.IM.player.nutrition -= self.IM.selecred_item.data.nutrition + 100
        # item in limbs/organs
        if state[1] == 'limb':
            self.IM.player.limbs.remove(self.IM.selecred_item.data)   
        elif state[1] == 'organ':
            self.IM.player.organs.remove(self.IM.selecred_item.data)

    def equip_item(self, state):
        # player has enough nutrition
        if hasattr(self.IM.selecred_item.data, 'nutrition'):
            if (self.IM.selecred_item.data.nutrition + 50 > self.IM.player.nutrition):
                print('equip_item: nutrition is too low') 
                self.IM.do_evrything.popup_window.open_popup('nutrition is too low')
                return
            else:
                self.IM.player.nutrition -= self.IM.selecred_item.data.nutrition + 50
        # equip
        if state[1] == 'storage':
            if hasattr(self.IM.selecred_item.data, 'limb_points'):
                self.IM.player.limbs.append(self.IM.selecred_item.data)
            elif hasattr(self.IM.selecred_item.data, 'organ_points'):
                self.IM.player.organs.append(self.IM.selecred_item.data)
            elif hasattr(self.IM.selecred_item.data, 'protection'):
                self.IM.player.armour = self.IM.selecred_item.data
            self.IM.player.storage.remove(self.IM.selecred_item.data)
        elif state[1] == 'loot':
            if hasattr(self.IM.selecred_item.data, 'limb_points'):
                self.IM.player.limbs.append(self.IM.selecred_item.data)
            elif hasattr(self.IM.selecred_item.data, 'organ_points'):
                self.IM.player.organs.append(self.IM.selecred_item.data)
            elif hasattr(self.IM.selecred_item.data, 'protection'):
                self.IM.player.armour = self.IM.selecred_item.data
            self.IM.buttons.loot_objects.remove(self.IM.selecred_item.data)

    def eat_item(self, state):
        self.IM.player.nutrition += self.IM.selecred_item.data.nutrition
        if state[1] == 'storage':
            self.IM.player.storage.remove(self.IM.selecred_item.data)
        elif state[1] == 'loot':
            self.IM.buttons.loot_objects.remove(self.IM.selecred_item.data)

    