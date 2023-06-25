import pygame as pg
import serial

class Joystick_test:
    def __init__(self, screen):
        self.port = 'com5'
        self.run = True
        self.fpsClock = pg.time.Clock()
        self.data = False

        self.ser = serial.Serial(self.port, 9600, timeout=0.05)
        self.ser.flush()

        self.size = (1280, 720)
        self.screen = screen
        self.screen_size = pg.display.get_surface().get_size()
        self.surface = pg.Surface(self.size)
        self.surface_size = (self.screen_size[0], int(self.screen_size[0]/self.surface_size[0]*self.surface_size[1]))

        self.joystick_surface = pg.Surface((510, 510))
        self.button_surface = pg.Surface((510,510))
    
    def close(self):
        self.ser.close()

    def start(self):
        while self.run:
            if self.ser.in_waiting > 0:
                try:
                    self.line = self.ser.readline().decode('euc-kr').rstrip()
                    self.data = list(map(int,self.line.split()))
                    self.joystick = [int(self.data[0]*0.5)+30, int(self.data[1]*0.5)+30, self.data[2]]
                    self.button = self.data[3:]
                except:
                    pass

            self.joystick_surface.fill((0,0,0))
            self.button_surface.fill((0,0,0))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        run = False

            if self.data:
                if self.joystick[-1]:
                    pg.draw.circle(self.joystick_surface, (255,255,255), self.joystick[:2], 30)
                else:
                    pg.draw.circle(self.joystick_surface, (255,255,255), self.joystick[:2], 30, 5)

                if self.button[0]:
                    pg.draw.circle(self.button_surface, (255,0,0), (255,100), 60)
                else:
                    pg.draw.circle(self.button_surface, (255,0,0), (255,100), 60, 10)

                if self.button[1]:
                    pg.draw.circle(self.button_surface, (255,255,0), (100,255), 60)
                else:
                    pg.draw.circle(self.button_surface, (255,255,0), (100,255), 60, 10)

                if self.button[2]:
                    pg.draw.circle(self.button_surface, (0,0,255), (255,410), 60)
                else:
                    pg.draw.circle(self.button_surface, (0,0,255), (255,410), 60, 10)

                if self.button[3]:
                    pg.draw.circle(self.button_surface, (0,255,0), (410,255), 60)
                else:
                    pg.draw.circle(self.button_surface, (0,255,0), (410,255), 60, 10)

            pg.draw.rect(self.joystick_surface, (255,255,255), (0, 0, 510, 510), 5)

            self.surface.blit(self.joystick_surface, (80,120))
            self.surface.blit(self.button_surface, (705, 120))
            self.screen.blit(pg.transform.scale(self.surface, self.surface_size), (0,0))

            pg.display.flip()
            self.fpsClock.tick(60)
        self.ser.close()