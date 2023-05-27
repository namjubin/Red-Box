import pygame as pg
from tool.widget.widget import *
pg.init()


class Main_menu:
    def __init__(self, screen):
        self.screen = screen

        self.setting()

    def setting(self):
        self.run = True
        self.fpsClock = pg.time.Clock()

    def start(self):
        while self.run:
            self.screen.fill((0,0,0))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.run = False

            pg.display.flip()
            self.fpsClock.tick(60)

pg.quit()