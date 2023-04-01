import pygame as pg
from random import *

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
        self.floor_speed = 0
        self.speed = 0
        self.jump = False
        self.up = False
        self.down = False
        self.score = 0
        self.obstacle_gauge = 0
        self.obstacle_taget = 100
        self.obstacle = []
        self.t_rex_loc = ()
        self.collision = False

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
        self.t_rex_over = self.get_img('T_Rex_Runner\T-Rex_image\T-Rex_over.png')

        self.cacti_small_1 = self.get_img('T_Rex_Runner\T-Rex_image\cacti_small_1.png')
        self.cacti_small_2 = self.get_img('T_Rex_Runner\T-Rex_image\cacti_small_2.png')
        self.cacti_small_3 = self.get_img('T_Rex_Runner\T-Rex_image\cacti_small_3.png')

        self.cacti_big_1 = self.get_img('T_Rex_Runner\T-Rex_image\cacti_big_1.png')
        self.cacti_big_2 = self.get_img('T_Rex_Runner\T-Rex_image\cacti_big_2.png')
        self.cacti_big_3 = self.get_img('T_Rex_Runner\T-Rex_image\cacti_big_3.png')

        self.ptera_1 = self.get_img('T_Rex_Runner\T-Rex_image\ptera_1.png')
        self.ptera_2 = self.get_img('T_Rex_Runner\T-Rex_image\ptera_2.png')

        self.obstacles = {'cacti_small_1' : self.cacti_small_1, 
                          'cacti_small_2' : self.cacti_small_2, 
                          'cacti_small_3' : self.cacti_small_3, 
                          'cacti_big_1' : self.cacti_big_1, 
                          'cacti_big_2' : self.cacti_big_2, 
                          'cacti_big_3' : self.cacti_big_3, 
                          'ptera' : [self.ptera_1, self.ptera_2]
                         }
        
        self.t_rex_over_mask = pg.mask.from_surface(self.t_rex_over)
        
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
            self.weight -= self.gravity * (1+self.main_rect[3]*0.002)
            self.gravity*=0.85

        elif self.down:
            self.weight += self.gravity * (1+self.main_rect[3]*0.002)
            self.gravity*=1.15

        if int(self.gravity) <= self.main_rect[3]*0.002 and self.up:
            self.up = False
            self.down = True
        
        elif self.weight >= 0 and self.down:
            self.weight = 0
            self.gravity = self.main_rect[3]/20
            self.up = False
            self.down = False
            self.jump = False

    def make_obstacles(self):
        self.obstacle_gauge += 1
        if self.obstacle_gauge >= self.obstacle_taget:
            self.obstacle_gauge = 0
            self.obstacle_taget = randint(40,71)
            obstacle = choice(list(self.obstacles.keys()))
            if obstacle == 'ptera':
                pass

            else:
                self.obstacle.append([self.obstacles[obstacle],[self.main_rect[0]+self.main_rect[2],(self.floor_rect[1]+self.floor_rect[3]*0.8)-self.obstacles[obstacle].get_height()]])

    def collide(self):
        x = self.obstacle[0][1][0] - self.t_rex_loc[0]
        y = self.obstacle[0][1][1] - self.t_rex_loc[1]

        if self.t_rex_over_mask.overlap(pg.mask.from_surface(self.obstacle[0][0]), (x,y)):
            self.collision = True
            self.runing = False

    def draw_game(self):
        if 0 < len(self.obstacle) and not self.collision and self.obstacle[0][1][0]-self.t_rex_loc[0]-self.t_rex_over.get_width()<=0 and self.obstacle[0][1][0]+self.obstacle[0][0].get_width()>=self.t_rex_loc[0]:
            self.collide()

        self.score_text = self.fontObj.render('%05d'%self.score, True, (80,80,80))
        self.score_text_rect = self.score_text.get_rect()
        self.score_text_rect[0], self.score_text_rect[1] = (self.main_rect[0]+self.main_rect[2])-self.score_text_rect[2], self.main_rect[1]
        self.screen.blit(self.score_text, self.score_text_rect)

        self.high_score_text = self.fontObj.render('HI %05d'%self.high_score, True, (120,120,120))
        self.high_score_text_rect = self.high_score_text.get_rect()
        self.high_score_text_rect[0], self.high_score_text_rect[1] = (self.score_text_rect[0]-self.high_score_text_rect[2]*1.1), self.main_rect[1]
        self.screen.blit(self.high_score_text, self.high_score_text_rect)
        
        if self.floor_speed+self.floor_rect[2]<=self.floor_img.get_width():
            self.floor_surface = self.floor_img.subsurface(pg.Rect(self.floor_speed,0,self.floor_rect[2],self.floor_img.get_height()))
            self.screen.blit(self.floor_surface, (self.floor_rect[0:2]))
        
        else:
            self.floor_surface = self.floor_img.subsurface(pg.Rect(self.floor_speed,0,self.floor_img.get_width()-self.floor_speed,self.floor_img.get_height()))
            self.screen.blit(self.floor_surface, (self.floor_rect[0:2]))
            self.floor_surface = self.floor_img.subsurface(pg.Rect(0,0,self.floor_rect[2]-self.floor_surface.get_width(),self.floor_img.get_height()))
            self.screen.blit(self.floor_surface, (self.floor_img.get_width()-self.floor_speed+self.floor_rect[0],self.floor_rect[1]))

        if self.jump:
                self.jump_func()

        if self.collision:
            for i in range(len(self.obstacle)):
                if self.obstacle[i][1][0] > self.main_rect[0]+self.main_rect[2]- self.obstacle[i][0].get_width():
                    obstacle_surface =  self.obstacles[self.obstacle[i][0]].subsurface(pg.Rect(0,0,(self.main_rect[0]+self.main_rect[2])-self.obstacle[i][1][0], self.obstacle[i][0].get_height()))
                    self.screen.blit(obstacle_surface, self.obstacle[i][1])

                elif self.obstacle[i][1][0] < self.main_rect[0]:
                    obstacle_surface =  self.obstacles[self.obstacle[i][0]].subsurface(pg.Rect(self.main_rect[0]-self.obstacle[i][1][0],0, self.obstacle[i][0].get_width()-(self.main_rect[0]-self.obstacle[i][1][0]), self.obstacle[i][0].get_height()))
                    self.screen.blit(obstacle_surface, (self.main_rect[0],self.obstacle[i][1][1]))

                else:
                    self.screen.blit(self.obstacle[i][0], self.obstacle[i][1])

            self.screen.blit(self.t_rex_over, self.t_rex_loc)

        elif self.runing:
            sub = 0

            for i in range(len(self.obstacle)):
                i -= sub
                self.obstacle[i][1][0] -= self.speed
                if self.obstacle[i][1][0] + self.obstacle[i][0].get_width() <= self.main_rect[0]:
                    sub +=1
                    self.obstacle.pop(i)
                    continue

                elif self.obstacle[i][1][0] > self.main_rect[0]+self.main_rect[2]- self.obstacle[i][0].get_width():
                    obstacle_surface =  self.obstacle[i][0].subsurface(pg.Rect(0,0,(self.main_rect[0]+self.main_rect[2])-self.obstacle[i][1][0], self.obstacle[i][0].get_height()))
                    self.screen.blit(obstacle_surface, self.obstacle[i][1])

                elif self.obstacle[i][1][0] < self.main_rect[0]:
                    obstacle_surface = self.obstacle[i][0].subsurface(pg.Rect(self.main_rect[0]-self.obstacle[i][1][0],0, self.obstacle[i][0].get_width()-(self.main_rect[0]-self.obstacle[i][1][0]), self.obstacle[i][0].get_height()))
                    self.screen.blit(obstacle_surface, (self.main_rect[0],self.obstacle[i][1][1]))

                else:
                    self.screen.blit(self.obstacle[i][0], self.obstacle[i][1])
                

            if self.jump:
                self.t_rex_loc = (self.main_rect[0]*2,(self.floor_rect[1]+self.floor_rect[3]*0.8)-self.t_rex_stop_img.get_height()+self.weight)
                self.screen.blit(self.t_rex_stop_img, self.t_rex_loc)

            elif self.state:
                self.t_rex_loc = (self.main_rect[0]*2,((self.floor_rect[1]+self.floor_rect[3]*0.8)-self.t_rex_run1_img.get_height()))
                self.screen.blit(self.t_rex_run1_img, self.t_rex_loc)

            else:
                self.t_rex_loc = (self.main_rect[0]*2,((self.floor_rect[1]+self.floor_rect[3]*0.8)-self.t_rex_run2_img.get_height()))
                self.screen.blit(self.t_rex_run2_img, self.t_rex_loc)

            if self.state_gauge >= 5:
                self.state = not self.state
                self.state_gauge = 0

            else:
                self.state_gauge += 1

            self.make_obstacles()

        else:
            self.screen.blit(self.t_rex_stop_img, (self.main_rect[0]*2,(self.floor_rect[1]+self.floor_rect[3]*0.8)-self.t_rex_stop_img.get_height()+self.weight))

    def set_speed(self, value):
        self.floor_speed = (self.floor_speed+self.size[0]//value)%self.floor_img.get_width()
        self.speed = self.size[0]//value

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
            
            if not self.jump and self.jump_start and not self.collision:
                self.runing = True

            if self.runing:
                self.set_speed(int(speed))
                self.score += 20/speed

                if speed >= 2:
                    speed *= 0.9999

            self.draw_game()

            pg.display.flip()
            self.fpsClock.tick(self.fps)

        #종료
        pg.quit()