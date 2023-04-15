import pygame as pg
from random import *
import os

class Tank:
    def __init__(self):
        self.Tank_img = pg.image.load('2D_Tank_game\Tank.png')

class TankGame:
    def __init__(self, screen, fps):
        self.screen = screen
        self.fps = fps
        self.run = True

    def start(self):
        while self.run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.run = False