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
        self.title = pg.transform.scale(self.title, (944, 190))
        self.title.set_alpha(0)
        self.sub_text = pg.image.load("./main_menu/img/sub_text.png")
        self.sub_text = pg.transform.scale(self.sub_text, (1077,125))

        self.icon_loc = [(self.surface_rect.width//2)-(self.icon.get_width()//2), 150]
        self.icon_rect = pg.Rect(0, 0, 1280, 920)

        self.title_loc = [(self.surface_rect.width//2)-(self.title.get_width()//2), 600]

        self.sub_text_loc = [(self.surface_rect.width//2)-(self.sub_text.get_width()//2), 800]

        self.intro = True
        self.w = 1
        self.title_show = False
        self.title_alpha = 0
        self.sub_text_show = False
        self.sub_text_alpha = 0

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
                if self.w < 70:
                    self.show_icon = pg.transform.scale(self.icon, (self.icon_rect.width-10*self.w, self.icon_rect.height-8*self.w))
                    self.icon_loc[0] += 5
                    self.icon_loc[1] += 1
                elif self.w == 80:
                    self.title_show = True
                elif self.title_alpha != 255:
                    self.title_alpha += 5
                    self.title.set_alpha(self.title_alpha)
                else:
                    self.sub_text_show = True
                    self.intor = False
                
                self.w += 1

            self.surface.blit(self.show_icon, self.icon_loc)

            if self.title_show:
                self.surface.blit(self.title, self.title_loc)
            if self.sub_text_show:
                self.surface.blit(self.sub_text, self.sub_text_loc)

            self.screen.blit(pg.transform.scale(self.surface, self.surface_size), self.surface_loc)

            pg.display.flip()
            self.fpsClock.tick(60)