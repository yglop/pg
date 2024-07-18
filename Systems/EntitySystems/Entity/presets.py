from Systems.EntitySystems.Entity.dataset import *

from copy import deepcopy


limbs_preset = {
    'base':[
        deepcopy(limbs['LimbArmHuman']),
        deepcopy(limbs['LimbArmHuman']), 
        deepcopy(limbs['LimbLegHuman']), 
        deepcopy(limbs['LimbLegHuman'])
        ],
}

organs_preset = {
    'base':[
        deepcopy(organs['HeartHuman']), 
        deepcopy(organs['LungsHuman']), 
        deepcopy(organs['LiverHuman']), 
        deepcopy(organs['DigestiveSystemHuman'])
        ],
}

equipment_preset = {
    'humanA': {
        'name':f'humanA',
        'armour':deepcopy(armour['ArmourP1']),
        'limbs':deepcopy(limbs_preset['base']),
        'organs':deepcopy(organs_preset['base']),
        'storage':[],
    },
    'humanB': {
        'name':f'humanB',
        'armour':None,
        'limbs':deepcopy(limbs_preset['base']),
        'organs':deepcopy(organs_preset['base']),
        'storage':[],
    },
}