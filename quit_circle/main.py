import pygame as pg

class Quit_circle:
    def __init__(self, screen, state1=True, state2=True):
        self.screen = screen
        self.state1 = state1
        self.state2 = state2
        self.screen_size = self.screen.get_size()
        self.surface = pg.Surface((400,400), pg.SRCALPHA)
        self.surface = self.surface.convert_alpha()
        self.surface_size = self.screen_size[1]//2
        self.surface_loc = (self.screen_size[0]//2-self.surface_size//2, self.screen_size[1]//2-self.surface_size//2)
        self.loc = 450
        self.state = 0

        self.font = pg.font.Font('./quit_circle/font/DungGeunMo.ttf',40)
        self.txt1 = self.font.render('종료', False, (255,255,255))
        self.font = pg.font.Font('./quit_circle/font/DungGeunMo.ttf',26)
        self.txt2 = self.font.render('메인화면', False, (255,255,255))
        self.txt1_loc = (20,180)
        self.txt2_loc = (285,187)
    def set_loc(self, loc):
        self.loc = loc
        if self.loc <= 0:
            self.state = 1
        elif self.loc >= 900:
            self.state = 2
        else:
            self.state = 0
        return self.state
    def show(self):
        if self.state == 1 and self.state1:
            pg.draw.circle(self.surface, (150,150,150), (200,200), 200, draw_top_left=True, draw_bottom_left=True)
        else:
            pg.draw.circle(self.surface, (100,100,100), (200,200), 200, draw_top_left=True, draw_bottom_left=True)
        if self.state == 2 and self.state2:
            pg.draw.circle(self.surface, (150,150,150), (200,200), 200, draw_top_right=True, draw_bottom_right=True)
        else:
            pg.draw.circle(self.surface, (100,100,100), (200,200), 200, draw_top_right=True, draw_bottom_right=True)
        
        pg.draw.circle(self.surface, (200,200,200), (200,200), 80)

        if self.state1:
            self.surface.blit(self.txt1, self.txt1_loc)
        if self.state2:
            self.surface.blit(self.txt2, self.txt2_loc)
        self.screen.blit(pg.transform.scale(self.surface, [self.surface_size,self.surface_size]), self.surface_loc)