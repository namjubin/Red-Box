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
        
        self.icon = pg.image.load("./main_menu/img/icon.png")
        self.title = pg.image.load("./main_menu/img/title.png")
        self.sub_text = pg.image.load("./main_menu/img/sub_text.png")

    def start(self):
        while self.run:
            self.screen.fill((255, 255, 255))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.run = False


            pg.display.flip()
            self.fpsClock.tick(60)