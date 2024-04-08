import pygame as pg


class TileVisual(pg.sprite.Sprite):
    def __init__(self, tile):
        super(TileVisual, self).__init__()
        self.tile_id = tile[0]
        self.image = tile[1]['image']
        self.rect = tile[1]['rect']
        self.rect.center = tile[1]['rect.center']
        self.clicked = False

    def update(self, event_list, do_evrything):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                self.clicked = not self.clicked

                do_evrything.try_move_player(self.tile_id)