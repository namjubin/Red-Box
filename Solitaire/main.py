import pygame as pg

class Card:
    def __init__(self, surface, card_front, card_back):
        self.surface = surface
        self.card_front = card_front
        self.card_back = card_back

        self.setting()

    def setting(self):
        self.card_front = pg.transform.scale(self.card_front, (100, 150))
        self.card_back = pg.transform.scale(self.card_back, (100, 150))
        self.open = False

    def set_location(self, left, top):
        self.left = left
        self.top = top

    def show(self):
        if self.open:
            self.surface.blit(self.card_front, (self.left, self.top))
        else:
            self.surface.blit(self.card_back, (self.left, self.top))

class Klondike:
    def __init__(self):
        pass

class Solitaire:
    def start(surface):
        ace_of_spades = pg.image.load('Solitaire/card_img/ace_of_spades2.png')
        card_back = pg.image.load('Solitaire/card_img/card_back.png')
        card = Card(surface, 100, 100, ace_of_spades, card_back)

        clock = pg.time.Clock()
        run = True

        while run:
            surface.fill((0,0,0))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        run = False
                    if event.key == pg.K_SPACE:
                        card.open = not card.open
                
            keys = pg.key.get_pressed()

            card.show()


            pg.display.flip()
            clock.tick(60)
