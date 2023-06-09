import pygame as pg
from random import *
import os
from quit_circle.main import Quit_circle

class T_Rex_Runner:
    def __init__(self, screen, joystick=False, fps=60):
        self.screen = screen
        self.joystick = joystick
        self.fps = fps
        self.screen_size = pg.display.get_surface().get_size()
        self.size = (800,600)
        self.fpsClock = pg.time.Clock()

        self.surface = pg.Surface((800, 600))
        self.surface_size = ((self.screen_size[1]/600)*800, self.screen_size[1])
        self.surface_loc = (self.screen_size[0]//2-self.surface_size[0]//2, 0)
        
        self.main_rect = (0, 0, 720, 180)
        self.main_surface = pg.Surface(self.main_rect[2:])

        self.show_rect = (40, 210)

        self.image_loc = os.getcwd()+'/'

        self.floor_img = pg.image.load('T_Rex_Runner/T-Rex_image/test.png').convert_alpha()
        self.floor_img = pg.transform.scale(self.floor_img,(1180, 19))
        self.floor_rect = (0, 142, 720, 19)
        
        self.t_rex_stop_img = self.get_img('T-Rex_stop.png')
        self.t_rex_run1_img = self.get_img('T-Rex_run1.png')
        self.t_rex_run2_img = self.get_img('T-Rex_run2.png')
        self.t_rex_over = self.get_img('T-Rex_over.png')

        self.cacti_small_1 = self.get_img('cacti_small_1.png')
        self.cacti_small_2 = self.get_img('cacti_small_2.png')
        self.cacti_small_3 = self.get_img('cacti_small_3.png')

        self.cacti_big_1 = self.get_img('cacti_big_1.png')
        self.cacti_big_2 = self.get_img('cacti_big_2.png')
        self.cacti_big_3 = self.get_img('cacti_big_3.png')

        self.ptera_1 = self.get_img('ptera_1.png')
        self.ptera_2 = self.get_img('ptera_2.png')

        self.obstacles = {'cacti_small_1' : self.cacti_small_1, 
                          'cacti_small_2' : self.cacti_small_2, 
                          'cacti_small_3' : self.cacti_small_3, 
                          'cacti_big_1' : self.cacti_big_1, 
                          'cacti_big_2' : self.cacti_big_2, 
                          'cacti_big_3' : self.cacti_big_3, 
                          'ptera' : self.ptera_1
                         }
        
        self.game_over = self.get_img('game_over.png')
        self.replay_button = self.get_img('replay_button.png')
        
        self.t_rex_over_mask = pg.mask.from_surface(self.t_rex_over)

        self.fontObj = pg.font.Font(self.image_loc+'T_Rex_Runner/font/PressStart2P-Regular.ttf', 14)

        self.setting()

    def setting(self):
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
        self.t_rex_loc = [15, 110]
        self.collision = False
        self.gravity = 9
        self.weight = 0

        self.quit_circle = Quit_circle(self.surface)
        self.quit_circle_state = False
        self.joystick_state = 0

        f = open(self.image_loc+'T_Rex_Runner/high_score.txt')
        self.high_score = int(f.readline())
        f.close()


    def get_img(self, img):
        img = pg.image.load(self.image_loc+'T_Rex_Runner/T-Rex_image/'+img).convert_alpha()
        img = pg.transform.scale(img,(int(img.get_width()*(self.main_rect[3]/350)),int(img.get_height()*(self.main_rect[3]/350))))
        return img

    def jump_func(self):
        if not self.collision:
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
                self.t_rex_loc[1] = 110
                self.weight = 0
                self.gravity = 9
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
                ptera_loc = randint(0,3)

                if ptera_loc == 0:
                    self.obstacle.append([self.obstacles[obstacle],[self.main_rect[0]+self.main_rect[2],self.main_rect[1]+self.main_rect[3]*0.2],0,False])

                elif ptera_loc == 1:
                    self.obstacle.append([self.obstacles[obstacle],[self.main_rect[0]+self.main_rect[2],self.main_rect[1]+self.main_rect[3]*0.5],0, False])

                else:
                    self.obstacle.append([self.obstacles[obstacle],[self.main_rect[0]+self.main_rect[2],self.main_rect[1]+self.main_rect[3]*0.6],0, False])

            else:
                self.obstacle.append([self.obstacles[obstacle],[self.main_rect[0]+self.main_rect[2],(self.floor_rect[1]+self.floor_rect[3]*0.8)-self.obstacles[obstacle].get_height()]])

    def collide(self):
        x = int(self.obstacle[0][1][0] - self.t_rex_loc[0])
        y = int(self.obstacle[0][1][1] - self.t_rex_loc[1])

        if self.t_rex_over_mask.overlap(pg.mask.from_surface(self.obstacle[0][0]), (x,y)):
            if self.high_score < self.score:
                f = open(self.image_loc+'T_Rex_Runner/high_score.txt', 'w')
                f.write(str(int(self.score)))
                f.close()

            self.collision = True
            self.runing = False

    def draw_game(self):
        if 0 < len(self.obstacle) and not self.collision and self.obstacle[0][1][0]-self.t_rex_loc[0]-self.t_rex_over.get_width()<=0 and self.obstacle[0][1][0]+self.obstacle[0][0].get_width()>=self.t_rex_loc[0]:
            self.collide()

        self.score_text = self.fontObj.render('%05d'%self.score, False, (80,80,80))
        self.score_text_rect = self.score_text.get_rect()
        self.score_text_rect[0], self.score_text_rect[1] = (self.main_rect[0]+self.main_rect[2])-self.score_text_rect[2], self.main_rect[1]
        self.main_surface.blit(self.score_text, self.score_text_rect)

        self.high_score_text = self.fontObj.render('HI %05d'%self.high_score, True, (120,120,120))
        self.high_score_text_rect = self.high_score_text.get_rect()
        self.high_score_text_rect[0], self.high_score_text_rect[1] = (self.score_text_rect[0]-self.high_score_text_rect[2]*1.1), self.main_rect[1]
        self.main_surface.blit(self.high_score_text, self.high_score_text_rect)
        
        if self.floor_speed+self.floor_rect[2]<=self.floor_img.get_width():
            self.main_surface.blit(self.floor_img, (0-self.floor_speed,self.floor_rect[1]))
        
        else:
            self.main_surface.blit(self.floor_img, (0-self.floor_speed,self.floor_rect[1]))
            self.main_surface.blit(self.floor_img, (0-self.floor_speed+self.floor_img.get_width(),self.floor_rect[1]))

        if self.jump:
                self.jump_func()

        if self.collision:
            for i in range(len(self.obstacle)):
                self.main_surface.blit(self.obstacle[i][0], self.obstacle[i][1])

            self.main_surface.blit(self.t_rex_over, self.t_rex_loc)

            self.main_surface.blit(self.game_over, [(self.main_rect[0]+self.main_rect[2]/2)-self.game_over.get_width()/2, self.main_rect[1]+self.main_rect[3]*0.3])
            self.main_surface.blit(self.replay_button, [(self.main_rect[0]+self.main_rect[2]/2)-self.replay_button.get_width()/2, self.main_rect[1]+self.main_rect[3]*0.5])

        elif self.runing:
            sub = 0

            for i in range(len(self.obstacle)):
                i -= sub
                self.obstacle[i][1][0] -= self.speed
                if self.obstacle[i][1][0] + self.obstacle[i][0].get_width() <= self.main_rect[0]:
                    sub +=1
                    self.obstacle.pop(i)
                    continue

                else:
                    self.main_surface.blit(self.obstacle[i][0], self.obstacle[i][1])

                if len(self.obstacle[i]) >= 3:
                    if self.obstacle[i][2] >= 15:
                        self.obstacle[i][2] = 0
                        self.obstacle[i][3] = not self.obstacle[i][3]

                        if self.obstacle[i][3]:
                            self.obstacle[i][0] = self.ptera_2
                        else:
                            self.obstacle[i][0] = self.ptera_1 
                    
                    else:
                        self.obstacle[i][2] += 1
                

            if self.jump:
                self.t_rex_loc = [15, int(110+self.weight)]
                self.main_surface.blit(self.t_rex_stop_img, self.t_rex_loc)

            elif self.state:
                self.main_surface.blit(self.t_rex_run1_img, self.t_rex_loc)

            else:
                self.main_surface.blit(self.t_rex_run2_img, self.t_rex_loc)

            if self.state_gauge >= 5:
                self.state = not self.state
                self.state_gauge = 0

            else:
                self.state_gauge += 1

            self.make_obstacles()

        else:
            self.t_rex_loc = [15, 110+self.weight]
            self.main_surface.blit(self.t_rex_stop_img, self.t_rex_loc)

    def set_speed(self, value):
        self.floor_speed = (self.floor_speed+self.size[0]//value)%self.floor_img.get_width()
        self.speed = self.size[0]//value

    def show(self):
        while self.run:
            self.main_surface.fill((255, 255, 255))
            self.surface.fill((255,255,255))
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.main_surface,(0,0))

            if self.joystick:
                if self.joystick.ser.in_waiting > 0:
                    data = self.joystick.value()
                    joystick_push = self.joystick.push(data)

                    self.quit_circle_state = data[2]
                    self.joystick_state = self.quit_circle.set_loc(data[0])

                    if joystick_push[0] and self.run:
                        if not self.jump:
                            self.jump_start = True
                            self.jump = True
                            self.up = True
                        
                        if self.collision:
                            self.runing = True
                            self.collision = False
                            self.setting()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.joystick.ser.close()
                    os._exit(os.EX_OK)

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.run = False
                    
                    if event.key == pg.K_SPACE and self.run:
                        if not self.jump:
                            self.jump_start = True
                            self.jump = True
                            self.up = True

                        if self.collision:
                            self.runing = True
                            self.collision = False
                            self.setting()
            
            if not self.jump and self.jump_start and not self.collision:
                speed = 100
                self.runing = True

            if self.runing:
                self.set_speed(int(speed))
                self.score += 20/speed

                if speed >= 2:
                    speed *= 0.9999

            self.draw_game()
            self.surface.blit(self.main_surface, (self.show_rect))

            if self.quit_circle_state:
                    self.quit_circle.show()
            else:
                if self.joystick_state == 1:
                    self.joystick.ser.close()
                    os._exit(os.EX_OK)
                if self.joystick_state == 2:
                    self.run = False

            self.screen.blit(pg.transform.scale(self.surface, self.surface_size), self.surface_loc)

            pg.display.flip()
            self.fpsClock.tick(self.fps)