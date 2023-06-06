from screeninfo import get_monitors
import pygame as pg
from Solitaire.main import Solitaire

# pygame 초기화
pg.init()

# 전체 화면
FULLSCREEN = False

if FULLSCREEN:
    for m in get_monitors():
        size = (m.width, m.height)
    screen = pg.display.set_mode(size, pg.FULLSCREEN)
else:
    screen_size = (800, 600)
    screen = pg.display.set_mode(screen_size)

solitaire = Solitaire()
solitaire.start(screen)