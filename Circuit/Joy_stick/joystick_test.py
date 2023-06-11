import pygame as pg
import serial

port = 'com3'
run = True
fpsClock = pg.time.Clock()
data = False

ser = serial.Serial(port, 9600, timeout=0.05)
ser.flush()

size = (1280, 720)
screen = pg.display.set_mode(size)
surface = pg.Surface(size)

joystick_surface = pg.Surface((510, 510))
button_surface = pg.Surface((510,510))

while run:
    if ser.in_waiting > 0:
        try:
            line = ser.readline().decode('euc-kr').rstrip()
            data = list(map(int,line.split()))
            joystick = [int(data[0]*0.5)+30, int(data[1]*0.5)+30, data[2]]
            button = data[3:]
        except:
            pass

    joystick_surface.fill((0,0,0))
    button_surface.fill((0,0,0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False

    if data:
        if joystick[-1]:
            pg.draw.circle(joystick_surface, (255,255,255), joystick[:2], 30)
        else:
            pg.draw.circle(joystick_surface, (255,255,255), joystick[:2], 30, 5)

        if button[0]:
            pg.draw.circle(button_surface, (255,0,0), (255,100), 60)
        else:
            pg.draw.circle(button_surface, (255,0,0), (255,100), 60, 10)

        if button[1]:
            pg.draw.circle(button_surface, (255,255,0), (100,255), 60)
        else:
            pg.draw.circle(button_surface, (255,255,0), (100,255), 60, 10)

        if button[2]:
            pg.draw.circle(button_surface, (0,0,255), (255,410), 60)
        else:
            pg.draw.circle(button_surface, (0,0,255), (255,410), 60, 10)

        if button[3]:
            pg.draw.circle(button_surface, (0,255,0), (410,255), 60)
        else:
            pg.draw.circle(button_surface, (0,255,0), (410,255), 60, 10)

    pg.draw.rect(joystick_surface, (255,255,255), (0, 0, 510, 510), 5)

    screen.blit(joystick_surface, (80,120))
    screen.blit(button_surface, (705, 120))

    pg.display.flip()
    fpsClock.tick(60)
    