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
        self.card_front = pg.transform.scale(self.card_front, (70, 100))
        self.card_back = pg.transform.scale(self.card_back, (70, 100))
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
    def start(self, surface):
        self.surface = surface
        sults = ['spades', 'diamonds', 'hearts', 'clubs']
        nums = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
        dir = 'Solitaire/img/card/'
        self.cards = []
        self.card_back = pg.image.load(dir+'card_back.png')

        self.empty_slot = pg.image.load(dir+'empty_slot.png')
        self.spades_slot = pg.image.load(dir+'spades_slot.png')
        self.diamonds_slot = pg.image.load(dir+'diamonds_slot.png')
        self.hearts_slot = pg.image.load(dir+'hearts_slot.png')
        self.clubs_slot = pg.image.load(dir+'clubs_slot.png')
        self.empty_slot = pg.transform.scale(self.empty_slot, (70, 100))
        self.spades_slot = pg.transform.scale(self.spades_slot, (70, 100))
        self.diamonds_slot = pg.transform.scale(self.diamonds_slot, (70, 100))
        self.hearts_slot = pg.transform.scale(self.hearts_slot, (70, 100))
        self.clubs_slot = pg.transform.scale(self.clubs_slot, (70, 100))

        self.card_location = [(95, 120), (185, 120), (275, 120), (365, 120), (455, 120), (545, 120), (635, 120)]

        for sult in sults:
            for num in nums:
                self.cards.append(Card(surface, pg.image.load(f'{dir}{num}_{sult}.png'), self.card_back, sult, num))

        clock = pg.time.Clock()
        run = True
        reset = True

        while run:
            if reset:
                cards = self.cards
                reset = False

            self.surface.fill((50, 201, 76))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        run = False
                    if event.key == pg.K_SPACE:
                        pass
                
            keys = pg.key.get_pressed()

            self.draw_board()

            pg.display.flip()
            clock.tick(60)

    def draw_board(self):
        self.surface.blit(self.empty_slot, self.card_location[0])
        self.surface.blit(self.empty_slot, self.card_location[1])
        self.surface.blit(self.empty_slot, self.card_location[2])
        self.surface.blit(self.empty_slot, self.card_location[3])
        self.surface.blit(self.empty_slot, self.card_location[4])
        self.surface.blit(self.empty_slot, self.card_location[5])
        self.surface.blit(self.empty_slot, self.card_location[6])