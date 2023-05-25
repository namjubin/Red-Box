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

run = True
fpsClock = pg.time.Clock()

img = pygame.image.load('T-Rex_stop.png')
print(type(screen))

btn1 = Button(screen, 100, 100, 100, 30, 'btn')
btn2 = Button(screen, 300, 100, 150, 30, 'state change')
img_btn = ImageButton(screen, 100, 150, img)
check = CheckBox(screen, 100, 270)
radio = RadioButton(screen, 150, 270)
radio1 = RadioButton(screen, 100, 320)
radio2 = RadioButton(screen, 150, 320)
radio3 = RadioButton(screen, 200, 320)
radio4 = RadioButton(screen, 250, 320)
bg = ButtonGroup(radio1, radio2, radio3, radio4)
label = Label(screen, 100, 370, 'this is a test', 40, (255,255,255))

def click():
    print('click')

def bg_click():
    state = bg.get_states()

    for i in range(len(state)):
        if state[i]:
            print(f'{i+1}번째 버튼 클릭')

def change():
    state = not btn1.visibility
    if state:
        btn1.enable()
        img_btn.enable()
        check.enable()
        radio.enable()
        bg.enable()
        label.enable()
    else:
        btn1.disabled()
        img_btn.disabled()
        check.disabled()
        radio.disabled()
        bg.disabled()
        label.disabled()

while run:
    mouse_loc = pg.mouse.get_pos()
    screen.fill((0,0,0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
        
        if event.type == pg.MOUSEBUTTONDOWN:
            btn1.if_click(mouse_loc, click)
            btn2.if_click(mouse_loc, change)
            img_btn.if_click(mouse_loc, click)
            check.if_click(mouse_loc, click)
            radio.if_click(mouse_loc, click)
            bg.if_click(mouse_loc, bg_click)

    btn1.show()
    btn2.show()
    img_btn.show()
    check.show()
    radio.show()
    radio1.show()
    radio2.show()
    radio3.show()
    radio4.show()
    label.show()

    pg.display.flip()
    fpsClock.tick(60)

pg.quit()