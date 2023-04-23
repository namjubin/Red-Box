import pygame as pg
from widget import *
import ctypes

pg.init()

FULLSCREEN = False

if FULLSCREEN:
    size = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
    screen = pg.display.set_mode(size, pg.FULLSCREEN)
else:
    screen_size = (800, 600)
    screen = pg.display.set_mode(screen_size)

def click():
    print('click')

run = True
fpsClock = pg.time.Clock()

btn1 = Button(screen, 100, 100, 100, 30, 'btn1', (255,255,255), 20, pg.Color(125,125,125), (255,255,255))

while run:
    mouse_loc = pg.mouse.get_pos()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
        
        if event.type == pg.MOUSEBUTTONDOWN:
            btn1.if_btn_click(mouse_loc, click)

        btn1.if_mouse_in(mouse_loc)

    btn1.show()

    pg.display.flip()
    fpsClock.tick(60)

pg.quit()