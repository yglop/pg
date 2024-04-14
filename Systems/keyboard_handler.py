import pygame as pg


def keyboard_handler(event_list, do_evrything):
    for event in event_list:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE and (event.mod & pg.KMOD_SHIFT):
                print('keyboard_handler: quit')
                pg.quit()   

            if do_evrything.inventory_menu.is_menu_open == False:
                if do_evrything.escape_menu.is_menu_open == False:
                    if event.key == pg.K_SPACE: 
                        do_evrything.TS.end_turn()
                    elif event.key == pg.K_ESCAPE:
                        do_evrything.escape_menu.open_menu()
                else:
                    if event.key == pg.K_ESCAPE:
                        do_evrything.escape_menu.close_menu()
            else:
                if event.key == pg.K_ESCAPE:
                    do_evrything.inventory_menu.close_menu()


    
