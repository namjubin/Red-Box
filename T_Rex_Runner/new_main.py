import pygame as pg
from random import *

def load_image(name):
    img = pg.image.load('T_Rex_Runner/T-Rex_image/'+name)
    img = pg.transform.scale(img, (img.get_width()*3, img.get_height()*3))
    return img

class T_Rex_Runner:
    def __init__(self, screen, fps=100):
        self.screen = screen
        self.fps = fps

        self.size = pg.display.get_surface().get_size()
        self.fpsClock = pg.time.Clock()

        self.run = True

    def start(self):
        while self.run:
            self.screen.fill((255, 255, 255))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.run = False

            pg.display.flip()
            self.fpsClock.tick(self.fps)

        #종료
        pg.quit()

pg.init()

if __name__ == "__main__":
    print('Hello')