import pygame as pg
from random import shuffle

class Card:
    def __init__(self, surface, card_front, card_back, sult, num):
        self.surface = surface
        self.card_front = card_front
        self.card_back = card_back
        self.sult = sult
        self.num = num

        self.setting()

    def setting(self):
        self.card_front = pg.transform.scale(self.card_front, (100, 150))
        self.card_back = pg.transform.scale(self.card_back, (100, 150))
        self.open = False
        self.state = False

    def select(self, state):
        self.state = state

    def set_location(self, left, top):
        self.left = left
        self.top = top

    def show(self):
        if self.state:
            pg.draw.rect(self.surface, (22, 106, 196), (self.left-5, self.top-5, 110, 160))
        if self.open:
            self.surface.blit(self.card_front, (self.left, self.top))
        else:
            self.surface.blit(self.card_back, (self.left, self.top))

class Klondike:
    def __init__(self):
        pass

class Solitaire:
    def start(surface):
        sults = ['spades', 'diamonds', 'hearts', 'clubs']
        nums = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
        dir = 'Solitaire/img/card/'
        cards = []
        card_back = pg.image.load('Solitaire/img/card/card_back.png')

        for sult in sults:
            for num in nums:
                cards.append(Card(surface, pg.image.load(f'{dir}{num}_{sult}.png'), card_back, sult, num))

        clock = pg.time.Clock()
        run = True

        while run:
            surface.fill((50, 201, 76))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        run = False
                    if event.key == pg.K_SPACE:
                        pass
                
            keys = pg.key.get_pressed()


            pg.display.flip()
            clock.tick(60)
