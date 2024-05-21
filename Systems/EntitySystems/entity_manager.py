import pygame as pg
import random

from Systems.EntitySystems.player_system import PlayerSystem
from Systems.EntitySystems.enemy_system import EnemySystem
from Systems.EntitySystems.items_system import ItemSystem
from Systems.EntitySystems.raycast import raycast

from Systems.EntitySystems.Entity.mob import Mob
from Systems.EntitySystems.Entity.Items.armour import *
from Systems.EntitySystems.Entity.Items.weapons_melee import *
from Systems.EntitySystems.Entity.Items.limbs import *
from Systems.EntitySystems.Entity.Items.organs import *

from Visuals.mob_visual import MobVisual
from Resources.Textures.dataset import player_sprite, enemy_sprite


class EntityManager():
    def __init__(self, MS):
        self.tile_map = MS.tile_map
        self.grid_size = MS.grid_size

        self.mobs_visual = dict()
        self.mobs_stats = dict()
        self.visible_mobs_visual = dict()
        self.interactable_dict = dict()
        self.interactable_id_count = 1000

        self.PS = PlayerSystem(self) 
        self.ES = EnemySystem(self)
        self.IS = ItemSystem()

        self.iterate_through_tile_map()

    def iterate_through_tile_map(self):
        for tile_id, tile_data in self.tile_map.items():
            if tile_data['mob'] == 2:
                self.append_mobs_visual(tile_data, sprite=player_sprite)
                self.append_mobs_stats(tile_id, ent_id=tile_data['mob'])
            elif tile_data['mob'] >= 100:
                self.append_mobs_visual(tile_data, sprite=enemy_sprite)
                self.append_mobs_stats(tile_id, ent_id=tile_data['mob'])
    
    def append_mobs_visual(self, tile_data, sprite):
        new_ent = MobVisual(sprite, tile_data['rect'], tile_data['rect.center'])
        self.mobs_visual[tile_data['mob']] = pg.sprite.RenderPlain(new_ent)
   
    def append_mobs_stats(self, tile_id, ent_id):
        limbs_preset = {
            'base':[LimbArmHuman(), LimbArmHuman(), LimbLegHuman(), LimbLegHuman()],
            'ling':[LimbArmHuman(), LimbArmBlade(), LimbLegHuman(), LimbLegHuman()],
            'armtest':[LimbArmHuman(), LimbArmHuman(), LimbArmHuman(), LimbArmHuman(), LimbArmHuman(), LimbArmHuman(), LimbArmHuman(), LimbArmHuman(), ], # debug
        }
        organs_preset = {
            'base':[HeartHuman(), LungsHuman(), LiverHuman(), DigestiveSystemHuman()],
        }
        equipment_preset = {
            'humanA': {
                'tile_id':tile_id,
                'name':f'humanA{str(ent_id)}',
                'armour':ArmourP1(),
                'limbs':limbs_preset['base'],
                'organs':organs_preset['base'],
                'storage':[],
            },
            'humanB': {
                'tile_id':tile_id,
                'name':f'humanB{str(ent_id)}',
                'armour':None,
                'limbs':limbs_preset['base'],
                'organs':organs_preset['base'],
                'storage':[],
            },
            'ling': {
                'tile_id':tile_id,
                'name':f'player',
                'armour':ArmourP1(),
                'limbs':limbs_preset['base'],
                'organs':organs_preset['base'],
                'storage':[Sword(),Sword(),Sword(),Sword(),Sword(),Sword(),Sword(),Sword(),],
            },
        }
        if ent_id == 2:
            self.mobs_stats[ent_id] = Mob(equipment_preset['ling'])
        else:
            self.mobs_stats[ent_id] = Mob(equipment_preset[random.choice(['humanA', 'humanB'])])

    def update_visible(self, screen):
        self.visible_mobs_visual.clear()
        self.visible_mobs_visual = raycast(self.tile_map, self.mobs_stats, self.visible_mobs_visual, screen)

    def render_ents(self, screen):
        for mob_id, mob_visual in self.mobs_visual.items():
            if mob_id == 2 or mob_id in self.visible_mobs_visual:
                mob_visual.draw(screen)
        self.update_visible(screen)
        
