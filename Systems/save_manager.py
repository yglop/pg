from Systems.EntitySystems.Entity.mob import Mob
from Systems.EntitySystems.Entity.dataset import *

from copy import deepcopy


class SaveManager():
    def __init__(self):
        self.player = None

    def load_save(self):
        data = None
        with open('./Saves/player.txt') as _f:
            data = _f.readlines()

        tile_id = data[0].strip('\n').split(',')
        tile_id[0], tile_id[1] = int(tile_id[0]), int(tile_id[1])
        
        _armour = deepcopy(armour[data[2].strip('\n')])

        _limbs = list()
        for i in data[3].strip('\n').split(','):
            _limbs.append(deepcopy(limbs[i]))
        
        _organs = list()
        for i in data[4].strip('\n').split(','):
            _organs.append(deepcopy(organs[i]))

        _storage = list()
        for i in data[5].strip('\n').split(','):
            _storage.append(deepcopy(all_items[i]))

        self.player = {
            'name':data[1].strip('\n'),
            'armour':_armour,
            'limbs':_limbs,
            'organs':_organs,
            'storage':_storage,
            'tile_id':tile_id,
        }
            