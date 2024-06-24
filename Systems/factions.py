import pygame as pg

from Systems.mission import Mission


class Factions():
    def __init__(self):
        self.reputation = [10, 10, 10, 10]
        self.missions0 = list()
        self.missions1 = list()
        self.missions2 = list()
        self.missions3 = list()

        self.add_mission()

    def add_mission(self):
        if self.reputation[0] >= 10:
            self.missions0.append(Mission('HE mission_10rep'))
        if self.reputation[0] >= 0:
            self.missions0.append(Mission('HE mission_0rep'))

        if self.reputation[1] >= 10:
            self.missions1.append(Mission('MA mission_10rep'))
        if self.reputation[1] >= 0:
            self.missions1.append(Mission('MA mission_0rep'))

        if self.reputation[2] >= 10:
            self.missions2.append(Mission('MFRC mission_10rep'))
        if self.reputation[2] >= 0:
            self.missions2.append(Mission('MFRC mission_0rep'))

        if self.reputation[3] >= 0:
            self.missions3.append(Mission('SWC mission_0rep'))

    def rep_change(self, change):
        for i in range(4):
            self.reputation[i] += change[i]
