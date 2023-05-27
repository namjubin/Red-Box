import pygame
import math

check_img = pygame.image.load('tool\widget\check.png')

def fill(surface, color):
    w, h = surface.get_size()
    r, g, b = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))

    return surface

class Button(pygame.Rect):
    def __init__(self, surface, left, top, width, height, text, text_color=(0,0,0), text_size=20, background=(255,255,255), accent=None, accent_size=None, font='None', antialias=True):
        super().__init__(left, top, width, height)
        self.surface = surface
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.text = text
        self.text_color = text_color
        self.text_size = text_size
        self.background = background
        self.accent = accent
        self.accent_size = accent_size
        self.font = font
        self.antialias = antialias

        self.setting()
    
    def setting(self):
        self.state = False
        self.visibility = True

        if self.font[-3:]=='ttf':
            font = pygame.font.Font(self.font, self.text_size)
        else:
            font = pygame.font.SysFont(self.font, self.text_size)

        self.text_render = font.render(self.text, self.antialias, self.text_color)
        self.text_rect = self.text_render.get_rect(center=self.center)

    def enable(self):
        self.visibility = True

    def disabled(self):
        self.visibility = False

    def if_mouse_in(self, mouse_loc):
        if self.visibility:
            if (self.left <= mouse_loc[0] <= self.left+self.width) and (self.top <= mouse_loc[1] <= self.top+self.height):
                self.set_state(True)
            else:
                self.set_state(False)

    def if_click(self, mouse_loc, func=False):
        if self.visibility:
            if (self.left <= mouse_loc[0] <= self.left+self.width) and (self.top <= mouse_loc[1] <= self.top+self.height):
                if func:
                    func()
                return True
            return False
    
    def set_state(self, state):
        self.state = state

    def show(self):
        if self.visibility:
            pygame.draw.rect(self.surface, self.background, self)
            self.surface.blit(self.text_render, self.text_rect)
            if self.state:
                pygame.draw.rect(self.surface, self.accent, self, self.accent_size)

class ImageButton(pygame.Rect):
    def __init__(self, surface, left, top, img, accent=None, accent_size=None):
        self.surface = surface
        self.left = left
        self.top = top
        self.img = img
        self.accent = accent
        self.accent_size = accent_size

        self.setting()

    def setting(self):
        self.state = False
        self.visibility = True

        try:
            self.width = int(self.img.get_width())
            self.height = int(self.img.get_height())
        except:
            print("이미지가 없습니다")
        super().__init__(self.left, self.top, self.width, self.height)

    def enable(self):
        self.visibility = True

    def disabled(self):
        self.visibility = False

    def if_mouse_in(self, mouse_loc):
        if self.visibility:
            if (self.left <= mouse_loc[0] <= self.left+self.width) and (self.top <= mouse_loc[1] <= self.top+self.height):
                self.set_state(True)
            else:
                self.set_state(False)

    def if_click(self, mouse_loc, func=False):
        if self.visibility:
            if (self.left <= mouse_loc[0] <= self.left+self.width) and (self.top <= mouse_loc[1] <= self.top+self.height):
                if func:
                    func()
                return True
            return False

    def set_state(self, state):
        self.state = state

    def show(self):
        if self.visibility:
            self.surface.blit(self.img, (self.left, self.top))
            if self.state:
                pygame.draw.rect(self.surface, self.accent, self, self.accent_size)

class CheckBox(pygame.Rect):
    def __init__(self, surface, left, top, length=30, background=(255,255,255), outline=(0,0,0), outline_size=2, select_color=(255,255,255), check_color=(0,0,0)):
        super().__init__(left, top, length, length)
        self.surface = surface
        self.left = left
        self.top = top
        self.length = length
        self.background = background
        self.outline = outline
        self.outline_size = outline_size
        self.select_color = select_color
        self.check_color = check_color

        self.setting()

    def setting(self):
        self.state = False
        self.visibility = True

        size = int(self.length * 0.7)
        self.check_img = pygame.transform.scale(check_img, (size, size))
        self.check_img = fill(self.check_img, self.check_color)

        self.check_loc = [(self.left + self.length // 2) - size // 2, (self.top + self.length // 2) - size // 2]

    def enable(self):
        self.visibility = True

    def disabled(self):
        self.visibility = False

    def if_click(self, mouse_loc, func=False):
        if self.visibility:
            if (self.left <= mouse_loc[0] <= self.left + self.length) and (self.top <= mouse_loc[1] <= self.top + self.length):
                self.set_state(not self.state)
                if func:
                    func()
                return True
            return False

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def show(self):
        if self.visibility:
            if self.state:
                pygame.draw.rect(self.surface, self.select_color, self)
                pygame.draw.rect(self.surface, self.outline, self, self.outline_size)
                self.surface.blit(self.check_img, self.check_loc)
            else:
                pygame.draw.rect(self.surface, self.background, self)
                pygame.draw.rect(self.surface, self.outline, self, self.outline_size)

class RadioButton(pygame.Rect):
    def __init__(self, surface, left, top, length=30, background=(255,255,255), outline=(0,0,0), outline_size=2, select_color=(0,0,0)):
        super().__init__(left, top, length, length)
        self.surface = surface
        self.left = left
        self.top = top
        self.length = length // 2
        self.background = background
        self.outline = outline
        self.outline_size = outline_size
        self.select_color = select_color

        self.setting()

    def setting(self):
        self.state = False
        self.visibility = True

        self.circle_size = int(self.length * 0.6)

    def enable(self):
        self.visibility = True

    def disabled(self):
        self.visibility = False

    def if_click(self, mouse_loc, func=False):
        if self.visibility:
            x = (mouse_loc[0] - self.center[0]) ** 2
            y = (mouse_loc[1] - self.center[1]) ** 2

            if math.sqrt(x+y) < self.length:
                self.set_state(not self.state)
                if func:
                    func()
                return True
            return False

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def show(self):
        if self.visibility:
            pygame.draw.circle(self.surface, self.background, self.center, self.length)

            if self.state:
                pygame.draw.circle(self.surface, self.select_color, self.center, self.length, self.outline_size)
                pygame.draw.circle(self.surface, self.select_color, self.center, self.circle_size)
            else:
                pygame.draw.circle(self.surface, self.outline, self.center, self.length, self.outline_size)

class ButtonGroup:
    def __init__(self, *buttons):
        self.buttons = list(buttons)

        self.setting()

    def setting(self):
        self.visibility = True
        self.value = [False for i in range(len(self.buttons))]

    def add(self, button):
        self.buttons.append(button)
        self.value.append(False)
        
    def remove(self, index):
        self.buttons.pop(index)
        self.value.pop(index)

    def enable(self):
        self.visibility = True
        for btn in self.buttons:
            btn.enable()

    def disabled(self):
        self.visibility = False
        for btn in self.buttons:
            btn.disabled()

    def if_click(self, mouse_loc, func=False):
        if self.visibility:
            for i in range(len(self.buttons)):
                if self.buttons[i].if_click(mouse_loc):
                    self.set_state(i)
                    if func:
                        func()
                    return True
            return False

    def set_state(self, index):
        self.value = [False for i in range(len(self.buttons))]
        self.value[index] = True

        for i in range(len(self.buttons)):
            if i == index:
                self.buttons[i].set_state(True)
            else:
                self.buttons[i].set_state(False)

    def get_state(self, index):
        return self.value[index]

    def get_states(self):
        return self.value
    
class Label(pygame.Rect):
    def __init__(self, surface, left, top, text, text_size, text_color, font='None', antialias=True):
        self.surface = surface
        self.left = left
        self.top = top
        self.text = text
        self.text_size = text_size
        self.text_color = text_color
        self.font = font
        self.antialias = antialias

        self.setting()

    def setting(self):
        self.visibility = True

        if self.font[-3:]=='ttf':
            font = pygame.font.Font(self.font, self.text_size)
        else:
            font = pygame.font.SysFont(self.font, self.text_size)
        
        self.text_render = font.render(self.text, self.antialias, self.text_color)

        super().__init__(self.left, self.top, self.text_render.get_width(), self.text_render.get_height())

    def enable(self):
        self.visibility = True

    def disabled(self):
        self.visibility = False

    def show(self):
        if self.visibility:
            self.surface.blit(self.text_render, self)