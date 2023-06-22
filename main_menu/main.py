import pygame as pg
from tool.widget.widget import *

from Circuit.Joy_stick.joystick_test import joystick_test
from T_Rex_Runner.main import T_Rex_Runner
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
        
        ### intro ###
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
        ### intro ###

        ### main_screen ###
        self.main_screen = False

        self.joystick_test = joystick_test(self.screen)
        self.T_rex_runner = T_Rex_Runner(self.screen)

        self.joystick_test_img = pg.image.load('./main_menu/img/joystick.png')
        self.T_rex_runner_img = pg.image.load('./main_menu/img/T-Rex_stop.png')

        self.joystick_test_img = pg.transform.scale(self.joystick_test_img, (200, 200))
        self.T_rex_runner_img = pg.transform.scale(self.T_rex_runner_img, (200, 200))

        self.joystick_test_btn = ImageButton(self.surface, 400, 100, self.joystick_test_img, (0,0,0), 5)
        self.T_rex_runner_btn = ImageButton(self.surface, 100, 100, self.T_rex_runner_img, (0,0,0), 5)

        self.joystick_test_btn.set_state(True)
        self.T_rex_runner_btn.set_state(True)

        
        ### main_screen ###

    def start(self):
        while self.run:
            if self.intro:
                self.screen.fill((255,255,255))
                self.surface.fill((255,255,255))

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.run = False

                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            self.run = False

                if self.w < 70:
                    self.show_icon = pg.transform.scale(self.icon, (self.icon_rect.width-10*self.w, self.icon_rect.height-8*self.w))
                    self.icon_loc[0] += 5
                    self.icon_loc[1] += 1
                elif self.w == 80:
                    self.title_show = True
                elif self.title_alpha != 255:
                    self.title_alpha += 5
                    self.title.set_alpha(self.title_alpha)
                elif self.w == 142:
                    self.sub_text_show = True
                elif self.w == 192:
                    self.intro = False
                    self.main_screen = True
                
                self.w += 1

                self.surface.blit(self.show_icon, self.icon_loc)
                if self.title_show:
                    self.surface.blit(self.title, self.title_loc)
                if self.sub_text_show:
                    self.surface.blit(self.sub_text, self.sub_text_loc)
            
            if self.main_screen:
                self.screen.fill((50,50,50))
                self.surface.fill((50,50,50))

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.run = False

                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            self.run = False


                self.T_rex_runner_btn.show()
                self.joystick_test_btn.show()

            self.screen.blit(pg.transform.scale(self.surface, self.surface_size), self.surface_loc)

            pg.display.flip()
            self.fpsClock.tick(60)