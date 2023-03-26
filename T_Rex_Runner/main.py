import pygame as pg
from random import *
import cv2 as cv


class T_Rex_Runner:
    def __init__(self, screen, fps=60):
        self.screen = screen
        self.fps = fps
        self.size = pg.display.get_surface().get_size()
        self.fpsClock = pg.time.Clock()
        self.run = True
        self.jump_start = False
        self.runing = False
        self.state = True
        self.state_gauge = 0.0
        self.speed = 0
        self.jump = False
        self.up = False
        self.down = False
        self.score = 0

        f = open('T_Rex_Runner/high_score.txt')
        self.high_score = int(f.readline())
        f.close()

        self.setting()

    def setting(self):
        ratio = self.size[0]/10

        self.main_rect = (ratio/2, (self.size[1]-((ratio*9/4)))/5*2, ratio*9, ratio*9/4)

        self.floor_img = pg.image.load('T_Rex_Runner/T-Rex_image/test.png').convert_alpha()
        self.floor_img = pg.transform.scale(self.floor_img,(self.floor_img.get_width()*(self.main_rect[3]/180),self.floor_img.get_height()*(self.main_rect[3]/180)))
        self.floor_rect = (self.main_rect[0], self.main_rect[3]+self.main_rect[1]-self.floor_img.get_height()*2, self.main_rect[2], self.floor_img.get_height())
        
        self.t_rex_stop_img = self.get_img('T_Rex_Runner\T-Rex_image\T-Rex_stop.png')
        self.t_rex_run1_img = self.get_img('T_Rex_Runner\T-Rex_image\T-Rex_run1.png')
        self.t_rex_run2_img = self.get_img('T_Rex_Runner\T-Rex_image\T-Rex_run2.png')

        self.cacti_small_1 = self.get_img('T_Rex_Runner\T-Rex_image\cacti_small_1.png')
        self.cacti_small_2 = self.get_img('T_Rex_Runner\T-Rex_image\cacti_small_2.png')
        self.cacti_small_3 = self.get_img('T_Rex_Runner\T-Rex_image\cacti_small_3.png')

        self.cacti_big_1 = self.get_img('T_Rex_Runner\T-Rex_image\cacti_big_1.png')
        self.cacti_big_2 = self.get_img('T_Rex_Runner\T-Rex_image\cacti_big_2.png')
        self.cacti_big_3 = self.get_img('T_Rex_Runner\T-Rex_image\cacti_big_3.png')

        self.ptera_1 = self.get_img('T_Rex_Runner\T-Rex_image\ptera_1.png')
        self.ptera_2 = self.get_img('T_Rex_Runner\T-Rex_image\ptera_2.png')

        
        self.gravity = self.main_rect[3]/20
        self.weight = 0

        self.fontObj = pg.font.Font('T_Rex_Runner/font/PressStart2P-Regular.ttf', int(self.main_rect[2]/50))

    def get_img(self, img):
        img = pg.image.load(img).convert_alpha()
        img = pg.transform.scale(img,(img.get_width()*(self.main_rect[3]/350),img.get_height()*(self.main_rect[3]/350)))
        return img

    def jump_func(self):
        self.state = True
        self.state_gauge = 0.0

        if self.up:
            self.weight -= self.gravity * 1.6
            self.gravity*=0.85

        elif self.down:
            self.weight += self.gravity * 1.6
            self.gravity*=1.15

        if int(self.gravity) <= 0 and self.up:
            self.up = False
            self.down = True
        
        elif self.weight >= 0 and self.down:
            self.weight = 0
            self.gravity = self.main_rect[3]/20
            self.up = False
            self.down = False
            self.jump = False

    def draw_game(self):
        #pg.draw.rect(self.screen, (0,255,0), self.main_rect)
        #pg.draw.rect(self.screen, (255,0,0), self.floor_rect)

        self.score_text = self.fontObj.render('%05d'%self.score, True, (80,80,80))
        self.score_text_rect = self.score_text.get_rect()
        self.score_text_rect[0], self.score_text_rect[1] = (self.main_rect[0]+self.main_rect[2])-self.score_text_rect[2], self.main_rect[1]
        self.screen.blit(self.score_text, self.score_text_rect)

        self.high_score_text = self.fontObj.render('HI %05d'%self.high_score, True, (120,120,120))
        self.high_score_text_rect = self.high_score_text.get_rect()
        self.high_score_text_rect[0], self.high_score_text_rect[1] = (self.score_text_rect[0]-self.high_score_text_rect[2]*1.1), self.main_rect[1]
        self.screen.blit(self.high_score_text, self.high_score_text_rect)
        
        if self.speed+self.floor_rect[2]<=self.floor_img.get_width():
            self.floor_surface = self.floor_img.subsurface(pg.Rect(self.speed,0,self.floor_rect[2],self.floor_img.get_height()))
            self.screen.blit(self.floor_surface, (self.floor_rect[0:2]))
        
        else:
            self.floor_surface = self.floor_img.subsurface(pg.Rect(self.speed,0,self.floor_img.get_width()-self.speed,self.floor_img.get_height()))
            self.screen.blit(self.floor_surface, (self.floor_rect[0:2]))
            self.floor_surface = self.floor_img.subsurface(pg.Rect(0,0,self.floor_rect[2]-self.floor_surface.get_width(),self.floor_img.get_height()))
            self.screen.blit(self.floor_surface, (self.floor_img.get_width()-self.speed+self.floor_rect[0],self.floor_rect[1]))

        if self.jump:
                self.jump_func()

        if self.runing and not self.jump:
            if self.state:
                self.screen.blit(self.t_rex_run1_img, (self.main_rect[0]*2,((self.floor_rect[1]+self.floor_rect[3]*0.8)-self.t_rex_run1_img.get_height())))

            else:
                self.screen.blit(self.t_rex_run2_img, (self.main_rect[0]*2,((self.floor_rect[1]+self.floor_rect[3]*0.8)-self.t_rex_run2_img.get_height())))

            if self.state_gauge >= 5:
                self.state = not self.state
                self.state_gauge = 0

            else:
                self.state_gauge += 1

        else:
            self.screen.blit(self.t_rex_stop_img, (self.main_rect[0]*2,(self.floor_rect[1]+self.floor_rect[3]*0.8)-self.t_rex_stop_img.get_height()+self.weight))

    def set_speed(self, value):
        self.speed = (self.speed+self.size[0]//value)%self.floor_img.get_width()

    def start(self):
        speed = 100

        while self.run:
            self.screen.fill((255, 255, 255))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.run = False
                    
                    if event.key == pg.K_SPACE and self.run:
                        if not self.jump:
                            self.jump_start = True
                            self.jump = True
                            self.up = True
            
            if not self.jump and self.jump_start:
                self.runing = True

            self.draw_game()

            if self.runing:
                self.set_speed(int(speed))
                self.score += 20/speed

                if speed >= 2:
                    speed *= 0.9999


            pg.display.flip()
            self.fpsClock.tick(self.fps)

        #종료
        pg.quit()