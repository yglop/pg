import pygame as pg
from Resources.Textures.dataset import tile_sprites_32


def lineRectIntersectionPoints(line, rect, tile_sprite):
    def linesAreParallel( x1,y1, x2,y2, x3,y3, x4,y4 ):
        # Return True if the given lines (x1,y1)-(x2,y2) and
        # (x3,y3)-(x4,y4) are parallel
        return (((x1-x2)*(y3-y4)) - ((y1-y2)*(x3-x4)) == 0)

    def intersectionPoint( x1,y1, x2,y2, x3,y3, x4,y4 ):
        # Return the point where the lines through (x1,y1)-(x2,y2) and
        # (x3,y3)-(x4,y4) cross.  This may not be on-screen
        #Use determinant method, as per
        Px = ((((x1*y2)-(y1*x2))*(x3 - x4)) - ((x1-x2)*((x3*y4)-(y3*x4)))) / (((x1-x2)*(y3-y4)) - ((y1-y2)*(x3-x4)))
        Py = ((((x1*y2)-(y1*x2))*(y3 - y4)) - ((y1-y2)*((x3*y4)-(y3*x4)))) / (((x1-x2)*(y3-y4)) - ((y1-y2)*(x3-x4)))
        return Px,Py

    ### Begin the intersection tests
    result = []
    line_x1, line_y1, line_x2, line_y2 = line   # split into components
    pos_x, pos_y, width, height = rect

    ### Convert the rectangle into 4 lines
    rect_lines = [(pos_x, pos_y, pos_x+width, pos_y), (pos_x, pos_y+height, pos_x+width, pos_y+height),  # top & bottom
                   (pos_x, pos_y, pos_x, pos_y+height), (pos_x+width, pos_y, pos_x+width, pos_y+height)] # left & right

    ### intersect each rect-side with the line
    for r in rect_lines:
        rx1,ry1,rx2,ry2 = r
        if (not linesAreParallel(line_x1,line_y1, line_x2,line_y2, rx1,ry1, rx2,ry2 )):    # not parallel
            pX, pY = intersectionPoint(line_x1,line_y1, line_x2,line_y2, rx1,ry1, rx2,ry2)  # so intersecting somewhere
            pX = round(pX)
            pY = round(pY)
            # Lines intersect, but is on the rectangle, and between the line end-points?
            if (rect.collidepoint(pX, pY)   and
                 pX >= min(line_x1, line_x2) and pX <= max(line_x1, line_x2) and
                 pY >= min(line_y1, line_y2) and pY <= max(line_y1, line_y2)
                 and tile_sprite == tile_sprites_32[1]):
                result.append((pX, pY))                                     # keep it
                if (len(result) == 1):
                    break   # Once we've found any intersection point, that's it
    return result

# Check to see if the Player can see any NPCs
def raycast(tile_map, mobs_stats, visible_mobs_visual, screen):      # DEBUG
    player_tile = tile_map[mobs_stats[2].tile_id]
    for mob_id, mob in mobs_stats.items():
        if mob_id == 2:
            continue
        mob_tile = tile_map[mob.tile_id]
        
        line_of_sight = [player_tile['rect.center'][0], player_tile['rect.center'][1], mob_tile['rect.center'][0], mob_tile['rect.center'][1]]
        flag = True
        for tile_id, tile_data in tile_map.items():
            intersection_points = lineRectIntersectionPoints(line_of_sight, tile_data['rect'], tile_data['image'])
            if (len(intersection_points) > 0):
                flag = False
                break # seen already
        
        if flag:
            #pg.draw.line(screen, (0,0,0,0), player_tile['rect.center'], mob_tile['rect.center'])
            visible_mobs_visual[mob_id] = mob
    return visible_mobs_visual
