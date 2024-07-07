from Systems.EntitySystems.Entity.Items.armour import *
from Systems.EntitySystems.Entity.Items.weapons_melee import *
from Systems.EntitySystems.Entity.Items.weapons_range import *
from Systems.EntitySystems.Entity.Items.limbs import *
from Systems.EntitySystems.Entity.Items.organs import *


limbs = {
    'LimbArmHuman':LimbArmHuman(),
    'LimbLegHuman':LimbLegHuman(),
    'LimbArmBlade':LimbArmBlade(),
}

organs = {
    'HeartHuman':HeartHuman(),
    'LungsHuman':LungsHuman(),
    'LiverHuman':LiverHuman(),
    'DigestiveSystemHuman':DigestiveSystemHuman(),
}

armour = {
    'ArmourP1':ArmourP1(),
}

other_items = {
    'Pistol':Pistol(),
    'Sword':Sword(),
}

all_items = {**limbs, **organs, **armour, **other_items}

