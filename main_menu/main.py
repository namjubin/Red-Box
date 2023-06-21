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
        self.surface_rect = pg.Rect(0, 0, 1600, 1200)
        self.surface = pg.Surface((self.surface_rect.width, self.surface_rect.height))
        self.surface_size = (int(self.surface_rect.width*(self.screen_size[1]/self.surface_rect.height)), self.screen_size[1])
        self.surface_loc = ((self.screen_size[0]//2)-(self.surface_size[0]//2), 0)
        
        self.icon = pg.image.load("./main_menu/img/icon.png")
        self.icon = pg.transform.scale(self.icon, (1280, 920))
        self.title = pg.image.load("./main_menu/img/title.png")
        self.sub_text = pg.image.load("./main_menu/img/sub_text.png")

        self.icon_loc = [(self.surface_rect.width//2)-(1280//2), 150]
        self.icon_rect = pg.Rect(0, 0, 1280, 920)

        self.intro = True
        self.w = 1

    def start(self):
        while self.run:
            self.screen.fill((255,255,255))
            self.surface.fill((255,255,255))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.run = False
            
            if self.intro:
                if self.w <= 120:
                    self.show_icon = pg.transform.scale(self.icon, (self.icon_rect.width-5*self.w, self.icon_rect.height-4*self.w))
                    self.icon_loc[0] += 2.5
                    self.icon_loc[1] += 1
                    self.w += 1

            self.surface.blit(self.show_icon, self.icon_loc)

            self.screen.blit(pg.transform.scale(self.surface, self.surface_size), self.surface_loc)

            pg.display.flip()
            self.fpsClock.tick(60)