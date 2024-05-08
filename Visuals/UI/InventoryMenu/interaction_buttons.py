import pygame as pg

from Visuals.Buttons.button_inventory_item import InteractionButton


class InteractionButtons():
    def __init__(self, IM):
        self.IM = IM

        self.interaction_buttons = pg.sprite.RenderPlain()

    def create_interaction_button(self, center, state):
        btn = InteractionButton(center=center, state=state)   
        self.interaction_buttons.add(btn)

    def degestive_system_check(self):
        for i in self.IM.player.organs:
            if i.organ_type == 'digestive':
                return True
        return False

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
            if hasattr(self.IM.selecred_item.data, 'nutrition') and self.degestive_system_check():
                btns_kwords.append('eat')
            kword = 'loot'
        elif self.IM.selecred_item.data in self.IM.player.storage:
            btns_kwords = ['drop', 'equip']
            if hasattr(self.IM.selecred_item.data, 'nutrition') and self.degestive_system_check():
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

    def popup(self, func_name ,text):
        print(f'{func_name}: {text}') 
        self.IM.do_evrything.popup_window.open_popup(text)

    def take_item(self, state):
        # storage has capacity for item
        if self.IM.selecred_item.data.weight + self.IM.player.storage_capacity > self.IM.player.max_storage_capacity:
            self.popup('take_item', 'storage has no space')
            return
        # player has action points
        if self.IM.player.actions <= 0:
            self.popup('take_item', 'no action points left')
            return
        # item is armour OR item in loot
        if state[1] == 'armour':
            self.IM.player.storage.append(self.IM.selecred_item.data)
            self.IM.player.armour = None
            self.IM.player.subtract_action(1)
            return
        elif state[1] == 'loot':
            self.IM.player.storage.append(self.IM.selecred_item.data)
            self.IM.buttons.loot_objects.remove(self.IM.selecred_item.data)
            self.IM.player.subtract_action(1)
            return
        # item in limbs or organs
        if self.IM.selecred_item.data.nutrition + 100 > self.IM.player.nutrition:
            self.popup('take_item', 'nutrition is too low')
            return
        else:
            self.IM.player.subtract_action(1)
            self.IM.player.nutrition -= self.IM.selecred_item.data.nutrition + 100
            self.IM.player.storage.append(self.IM.selecred_item.data)
            if state[1] == 'limb' :
                self.IM.player.limbs.remove(self.IM.selecred_item.data)
            elif state[1] == 'organ':
                self.IM.player.organs.remove(self.IM.selecred_item.data)

    def create_loot(self):
        self.IM.player.subtract_action(1)
        if self.IM.buttons.loot_objects:
            self.IM.buttons.loot_objects += [self.IM.selecred_item.data,]
        else:
            entity_manager = self.IM.do_evrything.EM
            self.IM.do_evrything.MS.tile_map[self.IM.player.tile_id]['loot'] = self.IM.do_evrything.EM.interactable_id_count
            entity_manager.interactable_dict[entity_manager.interactable_id_count] = [self.IM.selecred_item.data,]
            entity_manager.interactable_id_count += 1

    def drop_item(self, state):
        # player has action points
        if self.IM.player.actions <= 0:
            self.popup('drop_item', 'no action points left')
            return
        # item is armour OR item in storage
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
            self.popup('drop_item', 'nutrition is too low')
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
        if hasattr(self.IM.selecred_item.data, 'nutrition') and (self.IM.selecred_item.data.nutrition + 50 > self.IM.player.nutrition):
            self.popup('equip_item', 'nutrition is too low')
            return
        # player has action points
        if self.IM.player.actions <= 0:
            self.popup('equip_item', 'no action points left')
            return
        # equip
        if hasattr(self.IM.selecred_item.data, 'limb_points'):
            if self.IM.player.used_limb_points + self.IM.selecred_item.data.limb_points > self.IM.player.max_limb_points:
                self.popup('equip_item', 'not enough limb points')
                return
            self.IM.player.limbs.append(self.IM.selecred_item.data)
        elif hasattr(self.IM.selecred_item.data, 'organ_points'):
            if self.IM.player.used_organ_points + self.IM.selecred_item.data.organ_points > self.IM.player.max_organ_points:
                self.popup('equip_item', 'not enough organ points')
                return
            self.IM.player.organs.append(self.IM.selecred_item.data)
        elif hasattr(self.IM.selecred_item.data, 'hands_required'):
            if self.IM.player.used_hands + self.IM.selecred_item.data.hands_required > self.IM.player.hands:
                self.popup('equip_item', 'not enough hands')
                return
            self.IM.player.in_hands.append(self.IM.selecred_item.data)
            print(self.IM.player.in_hands) # debug
        elif hasattr(self.IM.selecred_item.data, 'protection'):
            if self.IM.player.armour:
                self.popup('equip_item', 'you already have armour')
                return
            self.IM.player.armour = self.IM.selecred_item.data
        # if item is equipped
        self.IM.player.nutrition -= (self.IM.selecred_item.data.nutrition + 50 if hasattr(self.IM.selecred_item.data, 'nutrition') else 50)
        self.IM.player.subtract_action(1)
        # delete
        if state[1] == 'storage':
            self.IM.player.storage.remove(self.IM.selecred_item.data)
        elif state[1] == 'loot':
            self.IM.buttons.loot_objects.remove(self.IM.selecred_item.data)

    def eat_item(self, state):
        # player has action points
        if self.IM.player.actions <= 0:
            self.popup('drop_item', 'no action points left')
            return
        self.IM.player.subtract_action(1)
        self.IM.player.nutrition += self.IM.selecred_item.data.nutrition
        if state[1] == 'storage':
            self.IM.player.storage.remove(self.IM.selecred_item.data)
        elif state[1] == 'loot':
            self.IM.buttons.loot_objects.remove(self.IM.selecred_item.data)

    