import pygame as pg
from tool.widget.widget import *
import sys

from joystick.joystick_test import Joystick
from T_Rex_Runner.main import T_Rex_Runner
from tetris.tetris import Tetris
from quit_circle.main import Quit_circle
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
        self.joystick = True
        ### intro ###

        ### main_screen ###
        self.main_screen = False

        try:
            self.joystick = Joystick(self.screen)
        except:
            self.joystick = False
            print("JoyStick Not Found")
        self.t_rex_runner = T_Rex_Runner(self.screen, self.joystick)
        self.tetris = Tetris(self.screen, self.joystick)
        self.quit_circle = Quit_circle(self.surface, state2=False)

        self.left_btn_loc = (100, 500)
        self.center_btn_loc = (550, 350)
        self.right_btn_loc = (1200, 500)

        self.joystick_img = pg.image.load('./main_menu/img/joystick.png')
        self.T_rex_runner_img = pg.image.load('./main_menu/img/T-Rex_stop.png')
        self.tetris_img = pg.image.load('./main_menu/img/tetris.png')

        self.joystick_bigimg = pg.transform.scale(self.joystick_img, (500, 500))
        self.T_rex_runner_bigimg = pg.transform.scale(self.T_rex_runner_img, (500, 500))
        self.tetris_bigimg = pg.transform.scale(self.tetris_img, (500, 500))

        self.joystick_img = pg.transform.scale(self.joystick_img, (300, 300))
        self.T_rex_runner_img = pg.transform.scale(self.T_rex_runner_img, (300, 300))
        self.tetris_img = pg.transform.scale(self.tetris_img, (300, 300))

        self.joystick_img.set_alpha(200)
        self.T_rex_runner_img.set_alpha(200)
        self.tetris_img.set_alpha(200)

        self.index = 0
        self.bigimg_list = [self.joystick_bigimg, self.T_rex_runner_bigimg, self.tetris_bigimg]
        self.img_list = [self.joystick_img, self.T_rex_runner_img, self.tetris_img]

        self.text_list = ['Joystick Test', 'T-Rex runner', 'Tetris']
        self.title_font = pg.font.Font('./main_menu/font/upheavtt.ttf', 150)
        self.title_list = []
        self.title_loc_list = []

        if self.joystick:
            self.game_list = [self.joystick.start, self.t_rex_runner.show, self.tetris.show]
            self.setting_list = [self.joystick.setting, self.t_rex_runner.setting, self.tetris.setting]
        else:
            self.game_list = [None, self.t_rex_runner.show, self.tetris.show]

        for text in self.text_list:
            title = self.title_font.render(text, True, (255,255,255))
            self.title_list.append(title)
            self.title_loc_list.append([(self.surface.get_width()//2)-(title.get_width()//2), 150])

        self.start_btn = Button(self.surface, 650, 950, 300, 100, 'start', text_size=80, background=(255,50,50), text_color=(255,255,255), accent=(100,0,0), accent_size=5, font='./main_menu/font/upheavtt.ttf')
        self.start_btn.set_state(True)

        self.quit_circle_state = False

        self.state = 0

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
                try:
                    if self.joystick:
                        if self.joystick.ser.in_waiting > 0:
                            data = self.joystick.value()
                            print(data)
                            joystick_push = self.joystick.push(data)
                            self.quit_circle_state = data[2]
                            self.state = self.quit_circle.set_loc(data[0])
                            if joystick_push[1]:
                                if self.index == 0:
                                    self.index = len(self.img_list)-1
                                else:
                                    self.index -= 1
                            if joystick_push[3]:
                                if self.index == len(self.img_list)-1:
                                    self.index = 0
                                else:
                                    self.index += 1
                            if joystick_push[2]:
                                try:
                                    self.game_list[self.index]()
                                    self.setting_list[self.index]()
                                except:
                                    print("게임 로딩 실패")
                except:
                    try:
                        self.joystick = Joystick(self.screen)
                        self.t_rex_runner = T_Rex_Runner(self.screen, self.joystick)
                        self.tetris = Tetris(self.screen, self.joystick)
                    except:
                        self.joystick = False

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.run = False

                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            self.run = False

                        if event.key == pg.K_LEFT:
                            if self.index == 0:
                                self.index = len(self.img_list)-1
                            else:
                                self.index -= 1
                        
                        if event.key == pg.K_RIGHT:
                            if self.index == len(self.img_list)-1:
                                self.index = 0
                            else:
                                self.index += 1
                        
                        if event.key == pg.K_SPACE:
                            try:
                                self.game_list[self.index]()
                                self.setting_list[self.index]()
                                
                            except:
                                print("게임 로딩 실패")
                
                pg.draw.rect(self.surface, (100,0,0), (535, 335, 530, 530))
                pg.draw.rect(self.surface, (255,50,50), (540, 340, 520, 520))
                self.surface.blit(self.bigimg_list[self.index], self.center_btn_loc)
                self.surface.blit(self.img_list[self.index-1], self.left_btn_loc)
                self.surface.blit(self.img_list[(self.index+1)%len(self.img_list)], self.right_btn_loc)
                self.surface.blit(self.title_list[self.index], self.title_loc_list[self.index])
                self.start_btn.show()

                if self.quit_circle_state:
                    self.quit_circle.show()
                else:
                    if self.state == 1:
                        self.run = False

            self.screen.blit(pg.transform.scale(self.surface, self.surface_size), self.surface_loc)

            pg.display.flip()
            self.fpsClock.tick(60)

        if self.joystick:
            self.joystick.ser.close()
        pygame.quit()