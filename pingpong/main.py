import pygame,sys
import time
import random

class Bar:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.rect = pygame.Rect(x, y, w, h)
        

    def up(self, value):
        if self.y > 0:
            self.y -= value
        else:
            self.y = 0
        self.rect.top = self.y

    def down(self, value):
        if self.y < size[1]-self.h:
            self.y += value
        else:
            self.y = size[1]-self.h
        self.rect.top = self.y

    def draw(self):
        pygame.draw.rect(main_surface, WHITE, self.rect, 0)

class Ball:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.rect = pygame.Rect(x-15, y-15, 30, 30)
    
    def ball_move(self):
        a = [1,-1,1,-1]
        global b_s_x, b_s_y,score_p2,score_p1
        if self.x + 15 >= 820:
            self.x = 400
            self.y = 250
            b_s_x *= random.choice(a)
            \
            b_s_y = random.randint(1,6)
            score_p1 += 1
        if self.x - 15 <= 0:
            self.x = 400
            self.y = 250
            b_s_x *= random.choice(a)
            b_s_y = random.randint(1,6)
            \
            score_p2 += 1
        
        if self.y + 15 >= 640  or self.y - 15 <= 0:
            b_s_y *= -1
        self.x += b_s_x
        self.y += b_s_y

        self.rect.left = self.x - 15
        self.rect.top = self.y - 15

    def draw(self):
        pygame.draw.rect(main_surface, BLACK, self.rect, 0)
        pygame.draw.circle(main_surface, WHITE, [self.x, self.y], 15, 0)

    

FPS = 60
clock = pygame.time.Clock()



BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,80,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

total_time = 5
start_ticks = pygame.time.get_ticks()
 




pygame.init()
size = (820, 640)
screen = pygame.display.set_mode(size)
#화면
main_surface = pygame.Surface(size)

bar1 = Bar(10, 290, 20, 100)
bar2 = Bar(790, 290, 20, 100)
ball = Ball(400, 250)

score_p1 = 0
score_p2 = 0

b_s_x = 6
b_s_y = -3
def draw_score():
    global font_test
    font_test = pygame.font.SysFont(None, 30)
    text_score = font_test.render("Score : " + str(score_p1), True, (255,255,0))
    screen.blit(text_score, [15,15])
    text_score2 = font_test.render("Score : " + str(score_p2), True, WHITE)
    screen.blit(text_score2, [715,15])
font_test = pygame.font.SysFont(None, 30)
run = True
def p1_win():
    font_win = pygame.font.SysFont(None, 60)
    win = font_win.render("Player 1 Win", True, WHITE)
    screen.blit(win, [screen.get_width()/2-80,screen.get_height()/2 - 15])
def p2_win():
    font_win = pygame.font.SysFont(None, 60)
    win = font_win.render("Player 2 Win", True, WHITE)
    screen.blit(win, [screen.get_width()/2-80,screen.get_height()/2 - 15])

def game_draw():
    font_win = pygame.font.SysFont(None, 60)
    win = font_win.render("DRAW", True, WHITE)
    screen.blit(win, [screen.get_width()/2-80,screen.get_height()/2 - 15])
while run:
    screen.fill(BLACK)
    main_surface.fill(BLACK)
    time.time()
    ball.ball_move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = font_test.render("TIME: " + str(int(total_time - elapsed_time)), True, (255,255,255))

    
    if bar1.rect.colliderect(ball.rect) or bar2.rect.colliderect(ball.rect):
        
        b_s_y = random.randint(1,9)
        b_s_x *= -1
        
    


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        bar2.up(15)
    if keys[pygame.K_DOWN]:
        bar2.down(15)
    if keys[pygame.K_w]:
        bar1.up(15)
    if keys[pygame.K_s]:
        bar1.down(15)
    
       

    bar1.draw()
    bar2.draw()
    ball.draw()
    #print(ball.y)
    
    print(score_p1," ",score_p2)
    screen.blit(main_surface, (0,0))
    draw_score()
    screen.blit(timer,(screen.get_width()/2-40,15))
    if total_time - elapsed_time <= 0:
        if score_p1 > score_p2:
            p1_win()
        elif score_p1 > score_p1:
            p2_win()
        elif score_p1 == score_p1:
            game_draw()
        run = False
    pygame.display.update()
    
    clock.tick(FPS)
pygame.time.delay(2000)
pygame.quit()
quit()