from Systems.EntitySystems.Entity.dataset import *

limbs_preset = {
    'base':[limbs['LimbArmHuman'], limbs['LimbArmHuman'], limbs['LimbLegHuman'], limbs['LimbLegHuman']],
    'ling':[limbs['LimbArmHuman'], limbs['LimbArmBlade'], limbs['LimbLegHuman'], limbs['LimbLegHuman']],
}

organs_preset = {
    'base':[organs['HeartHuman'], organs['LungsHuman'], organs['LiverHuman'], organs['DigestiveSystemHuman']],
}

equipment_preset = {
    'humanA': {
        'name':f'humanA',
        'armour':armour['ArmourP1'],
        'limbs':limbs_preset['base'],
        'organs':organs_preset['base'],
        'storage':[],
    },
    'humanB': {
        'name':f'humanB',
        'armour':None,
        'limbs':limbs_preset['base'],
        'organs':organs_preset['base'],
        'storage':[],
    },
    'ling': {
        'name':f'player',
        'armour':ArmourP1(),
        'limbs':limbs_preset['ling'],
        'organs':organs_preset['base'],
        'storage':[other_items['Pistol'], other_items['Sword']],
    },
}