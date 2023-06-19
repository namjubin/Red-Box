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
        self.screen_size = pg.display.get_surface().get_size()
        self.logo = pg.image.load('.\main_menu\img\LOGO.png')
        dis = self.logo.get_height()//3
        dis = [int(self.logo.get_width()*(dis/self.screen_size[1])), dis]
        self.logo = pg.transform.scale(self.logo, dis)
        self.loc = [(self.screen_size[0]-self.logo.get_width())//2, (self.screen_size[1]-self.logo.get_height())//2]

    def start(self):
        while self.run:
            self.screen.fill((255, 255, 255))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.run = False

            self.screen.blit(self.logo, self.loc)

            pg.display.flip()
            self.fpsClock.tick(60)