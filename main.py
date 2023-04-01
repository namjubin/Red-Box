import pygame as pg
import ctypes
from T_Rex_Runner.main import *

#pygame 초기화
pg.init()

#전체 화면
full_screen = False   

if full_screen:
    u32 = ctypes.windll.user32
    size = u32.GetSystemMetrics(0), u32.GetSystemMetrics(1)
    screen = pg.display.set_mode(size, pg.FULLSCREEN)

else:
    size = (800, 600)
    screen = pg.display.set_mode(size)

t_rex = T_Rex_Runner(screen)
t_rex.start()  