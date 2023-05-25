import pygame

class Button(pygame.Rect):
    def __init__(self, surface, left, top, width, height, text, text_color, text_size, background, accent, font='None', antialias=True):
        super().__init__(left, top, width, height)
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.surface = surface
        self.text = text
        self.text_color = text_color
        self.text_size = text_size
        self.background = background
        self.accent = accent
        self.font = font
        self.antialias = antialias

        self.set_button()
    
    def set_button(self):
        self.state = False

        if self.font[-3:]=='ttf':
            font = pygame.font.Font(self.font, self.text_size)
        else:
            font = pygame.font.SysFont(self.font, self.text_size)

        self.text_render = font.render(self.text, self.antialias, self.text_color)
        self.text_rect = self.text_render.get_rect(center=self.center)

    def if_mouse_in(self, mouse_loc):
        if (self.left <= mouse_loc[0] <= self.left+self.width) and (self.top <= mouse_loc[1] <= self.top+self.height):
            self.select(True)
        else:
            self.select(False)

    def if_btn_click(self, mouse_loc, func):
        if (self.left <= mouse_loc[0] <= self.left+self.width) and (self.top <= mouse_loc[1] <= self.top+self.height):
            func()
    
    def select(self, state):
        self.state = state

    def show(self):
        pygame.draw.rect(self.surface, self.background, self)
        self.surface.blit(self.text_render, self.text_rect)
        if self.state:
            pygame.draw.rect(self.surface, self.accent, self, 3)

class CheckBox(pygame.Rect):
    def __init__(self):
        pass