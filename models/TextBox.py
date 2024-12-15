import pygame
from pygame import font, Surface, Rect
from resources import colors

font.init()


class TextBox():
    txt_font = font.Font("resources/fonts/Quicksand-Regular.ttf", 20)

    def __init__(self,
                 root,
                 pos, size,
                 base_fore_color,
                 base_back_color,

                 ):

        self.root = root
        self.pos = pos
        self.size = size
        self.text = ""

        self.base_back_color = base_back_color,
        self.base_fore_color = base_fore_color

        self.focused = False
        self.action = None

    def txt_surface(self):
        fore_color = ()
        back_color = ()

        fore_color = self.base_fore_color
        back_color = self.base_back_color

        surf = Surface(self.size)
        surf.fill(self.base_back_color)
        text_surf = self.txt_font.render(self.text, True, fore_color)
        text_rect = text_surf.get_rect(center=surf.get_rect().center)

        if self.focused:
            pygame.draw.line(surf, colors.SKY_BLUE, (2, self.size[1]-10),
                         (self.size[0]-2, self.size[1]-10), 2)
        surf.blit(text_surf, (2, text_rect.y))
        return surf

    def point_in_bound(self, point):
        pos = self.pos
        size = self.size
        rect = (pos[0], pos[1], pos[0] + size[0], pos[1] + size[1])

        return rect[0] <= point[0] <= rect[2] and rect[1] <= point[1] <= rect[3]

    def update(self):
        self.root.blit(self.txt_surface(), self.pos)

    def left_mouse_down_listener(self, point):
        if self.point_in_bound(point):
            self.focused = not self.focused

        else:
            self.focused = False

    def key_down_listener(self, key):
        if not self.focused:
            return
        if key == 8:
            if len(self.text)> 0:
                self.text = self.text[:-1]
        elif 48 <= key <= 57:
            self.text += chr(key)
