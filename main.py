import ctypes
import pygame as pg
from T_Rex_Runner.main import T_Rex_Runner

# pygame 초기화
pg.init()

# 전체 화면
FULLSCREEN = False

if FULLSCREEN:
    size = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
    screen = pg.display.set_mode(size, pg.FULLSCREEN)
else:
    screen_size = (800, 600)
    screen = pg.display.set_mode(screen_size)

# T-Rex Runner 게임 실행
t_rex = T_Rex_Runner(screen)
t_rex.start()