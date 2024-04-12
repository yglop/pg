import random
import numpy as np

from Mapgen.rectangular_room import RectangularRoom
from Mapgen.tunnel_between import tunnel_between


def generate_map(
        max_rooms=20,
        room_min_size=3,
        room_max_size=12,
        map_width=30,
        map_height=30,
    ):
    game_map = np.full((map_width, map_height), fill_value=0, order="F")
    
    rooms = []

    for i in range(max_rooms):
        room_width = random.randint(room_min_size, room_max_size)
        room_height = random.randint(room_min_size, room_max_size)

        x = random.randint(0, map_width - room_width - 1)
        y = random.randint(0, map_height - room_height - 1)

        # "RectangularRoom" class makes rectangles easier to work with
        new_room = RectangularRoom(x, y, room_width, room_height)

        game_map[slice(*new_room.inner()[0]), slice(*new_room.inner()[1])] = 9

        # draw player
        if len(rooms) == 0:
            game_map[new_room.center()] = 1
        else:
            # draw tonnels
            for x, y in tunnel_between(rooms[-1].center(), new_room.center()):
                if game_map[x, y] not in [1, 9]:
                    game_map[x, y] = 8
        
        # check for player id(1) 
        is_player = False
        for _ in game_map:
            if 1 in _:
                is_player = True
        if is_player == False:
            game_map[new_room.center()] = 1

        # create enamy ent
        if 1 not in game_map[slice(*new_room.inner()[0]), slice(*new_room.inner()[1])]:
            enamys_per_room = random.randint(1, (room_width * room_height) // 4)
            while enamys_per_room > 0:
                x = random.randint(new_room.inner()[0][0], new_room.inner()[0][1])
                y = random.randint(new_room.inner()[1][0], new_room.inner()[1][1])
                game_map[x, y] = 2
                
                enamys_per_room -= 1

        rooms.append(new_room)

    return(game_map)