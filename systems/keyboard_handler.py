import pygame as pg


def keyboard_handler(event_list, do_evrything):
    for event in event_list:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE: 
                do_evrything.TS.end_turn()
                


    
