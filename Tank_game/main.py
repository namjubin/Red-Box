import pygame as pg
from random import *
import os

class Tank:
    def __init__(self, surface, img_name, size):
        self.surface = surface
        self.img_name = img_name
        self.size = size

        self.setting()
    
    def setting(self):
        self.tank = pg.image.load(self.img_name)
    
    def show(self):
        self.surface.blit(self.tank, [500,300])

class Tank_game:
    def start(surface):
        t1 = Tank(surface, 'Tank_game/img/1_Tank.png', [0,0])

        clock = pg.time.Clock()
        run = True

        while run:
            surface.fill((0,0,0))
            t1.show()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        run = False
                
            keys = pg.key.get_pressed()


            pg.display.flip()
            clock.tick(60)

pg.quit()
            