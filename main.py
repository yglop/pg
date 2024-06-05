import pygame as pg
from do_everything import DoEvrything

from Systems.keyboard_handler import keyboard_handler

from Visuals.UI.hub import HubMenu
from Visuals.UI.escape_menu import EscapeMenu


pg.init()
screen = pg.display.set_mode((1200, 1000))
#screen.fill((100,100,100))

clock = pg.time.Clock()        

do_evrything = DoEvrything(screen)
hub_menu = HubMenu(screen)
escape_menu = EscapeMenu(screen)

# Main loop
running = True
while running:   
    clock.tick(60)
    
    event_list = pg.event.get()
    keyboard_handler(event_list, do_evrything, escape_menu)
    # Check events
    for event in event_list:
        if event.type == pg.QUIT:
            running = False

    if escape_menu.is_menu_open:
        escape_menu.draw_menu(event_list)
        pg.display.flip()
        continue       
    if hub_menu.is_open:
        hub_menu.render_all()
        pg.display.flip()
        continue 
    
    do_evrything.runner(event_list)
    pg.display.flip()
# close pygame
pg.quit()
exit()