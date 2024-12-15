import pygame
from pygame import Rect, font, Surface

from resources import colors

font.init()


class Cell:
    Size = 50
    Margin = 1
    cell_font = font.Font("resources/fonts/Quicksand-Regular.ttf", 20)

    def __init__(self, root, x, y, action):
        self.root = root
        self.x = x
        self.y = y
        self.gx = self.x * self.Size
        self.gy = self.y * self.Size
        self.is_wall = False
        self.action = action
        self.surface = Surface((self.Size, self.Size), pygame.SRCALPHA)
        self.value = ""
        self.branches = []
        self.color = colors.WHITE

    def reset(self):
        self.is_wall = False
        self.value = ""
        self.branches = []
        self.color = colors.WHITE

    def update_surf(self):

        if not self.is_wall:
            self.surface.fill(self.color)
        else:
            self.surface.fill(colors.BLACK)

        text_surf = self.cell_font.render(self.value, True, colors.BLACK)
        text_rect = text_surf.get_rect(center=self.surface.get_rect().center)
        self.surface.blit(text_surf, text_rect)

    def get_rect(self):
        return Rect(self.gx, self.gy, self.Size, self.Size)

    def click_in_bound(self, point):
        return self.get_rect().collidepoint(point)

    def left_mouse_down_listener(self, point):
        if not self.click_in_bound(point):
            return
        if self.action:
            self.action(self)

    def draw(self):
        self.update_surf()
        self.root.blit(self.surface, (self.gx, self.gy))
        pygame.draw.rect(self.root, colors.GRAY, self.get_rect(), 2)

    def draw_mask(self, color):
        pygame.draw.rect(self.surface, color, self.get_rect())
        self.root.blit(self.surface, (self.gx, self.gy))

    def add_char(self, char):
        if len(self.value) < 2:
            self.value += char

    def del_char(self):
        self.value = self.value[:-1]
