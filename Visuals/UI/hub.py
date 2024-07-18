import pygame as pg

from Systems.factions import Factions

from Visuals.Buttons.Hub.button_inventory import HubInventoryButton
from Visuals.Buttons.Hub.button_mission import HubMissionButton


class HubMenu():
    def __init__(self, screen):
        self.screen = screen

        self.arial16 = pg.font.Font('./Resources/Fonts/arial_bold.ttf', 16)
        self.arial24 = pg.font.Font('./Resources/Fonts/arial_bold.ttf', 24)
        self.sga24 = pg.font.Font('./Resources/Fonts/enchantment-proper.ttf', 24)
        self.text_colour = (30, 30, 30)

        self.factions = Factions()
        self.is_open = True # DEBUG

        self.buttons_first_column = pg.sprite.RenderPlain()
        self.buttons_missions = pg.sprite.RenderPlain()
        self.cerate_buttons()

        self.selected_mission = None 

    def create_button_mission(self, pos, mission):
        misson_button = HubMissionButton(pos, mission)
        self.buttons_missions.add(misson_button)
        pos[1] += 34

    def cerate_buttons(self):
        inventory_button = HubInventoryButton((20,20))
        self.buttons_first_column.add(inventory_button)
        pos = [572, 70] 
        for i in self.factions.missions0:
            self.create_button_mission(pos, i)
        pos[1] = 170
        for i in self.factions.missions1:
            self.create_button_mission(pos, i)
        pos[1] = 270
        for i in self.factions.missions2:
            self.create_button_mission(pos, i)
        pos[1] = 374
        for i in self.factions.missions3:
            self.create_button_mission(pos, i)
        
    ## renders
    def draw_rectangles(self):
        self.screen.fill((200,255,200))
        pg.draw.rect(self.screen, (200,200,255), pg.Rect(0, 0, 400, 1000))

    def blint_second_column_text(self, text, pos, reputation):
        self.screen.blit(text, pos)
        text = self.arial16.render(str(reputation), False, self.text_colour)
        self.screen.blit(text, (pos[0]+600, pos[1]+10))
        pos[1] += 100

    def render_text(self):
        # first column
        pos = [20, 80]
        text = self.arial16.render(f'some text', False, self.text_colour)
        self.screen.blit(text, pos)
        # second column
        pos = [420, 20]
        text = self.arial24.render(f'Hazard Extraction', False, self.text_colour)
        self.blint_second_column_text(text, pos, self.factions.reputation[0])
        text = self.arial24.render(f'Miliarium Adamantium', False, self.text_colour)
        self.blint_second_column_text(text, pos, self.factions.reputation[1])
        text = self.arial24.render(f'Metropoly Fleet Reserch Corp', False, self.text_colour)
        self.blint_second_column_text(text, pos, self.factions.reputation[2])
        text = self.sga24.render(f'Space Wizards Confederation', False, self.text_colour)
        self.blint_second_column_text(text, pos, self.factions.reputation[3])

    def render_mission_btn_text(self):
        for i in self.buttons_missions:
            text = self.arial16.render(i.text, False, self.text_colour)
            self.screen.blit(text, i.text_center)

    def render_buttons(self, event_list):
        #self.buttons_first_column.update(event_list, self) # ToDO
        self.buttons_first_column.draw(self.screen)
        self.buttons_missions.draw(self.screen)
        self.buttons_missions.update(event_list, self)
        self.render_mission_btn_text()

    def start_the_game(self):
        self.factions.rep_change(self.selected_mission.rep_change)
        self.is_open = False
        print(f'HUB: mission is selected: {self.selected_mission.name}')

    def render_all(self, event_list):
        self.draw_rectangles()
        self.render_text()
        self.render_buttons(event_list)

        if self.selected_mission:
            self.start_the_game()
            return True
        return False       
