import pygame as pg
from do_everything import DoEvrything


pg.init()
screen = pg.display.set_mode((1200, 800))
screen.fill((100,100,100))

clock = pg.time.Clock()        

do_evrything = DoEvrything()

# Main loop
running = True
while running:   
    clock.tick(60)
    
    event_list = pg.event.get()
    # Check events
    for event in event_list:
        if event.type == pg.QUIT:
            running = False

    do_evrything.runner(event_list, screen)

    pg.display.flip()

# close pygame
pg.quit()
exit()