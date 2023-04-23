from screeninfo import get_monitors
import pygame as pg
from T_Rex_Runner.main import T_Rex_Runner

# pygame 초기화
pg.init()

# 전체 화면
FULLSCREEN = True

if FULLSCREEN:
    for m in get_monitors():
        size = (m.width, m.height)
    screen = pg.display.set_mode(size, pg.FULLSCREEN)
else:
    screen_size = (800, 600)
    screen = pg.display.set_mode(screen_size)

# T-Rex Runner 게임 실행
t_rex = T_Rex_Runner(screen)
t_rex.start()