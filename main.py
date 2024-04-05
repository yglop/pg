import pygame as pg
from do_everything import DoEvrything


pg.init()
actual_screen = pg.display.set_mode((1200, 800))
game_screen = pg.Surface((1000, 800))
ui_screen = pg.Surface((200, 800))

game_screen.fill((100,100,100))
ui_screen.fill((0,0,100))
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

    do_evrything.runner(event_list, game_screen, ui_screen)

    actual_screen.blit(game_screen, (0, 0))
    actual_screen.blit(ui_screen, (1000, 0))
    pg.display.flip()

# close pygame
pg.quit()
exit()