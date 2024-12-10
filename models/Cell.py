import pygame
from pygame import Rect

from resources.colors import GRAY, WHITE, BLACK


class Cell:
    Size = 50
    Margin = 1

    def __init__(self, root, x, y, action):
        self.root = root
        self.x = x
        self.y = y
        self.is_wall = False
        self.is_temp_wall = False
        self.visited = False
        self.rect = Rect(x*self.Size, y*self.Size, self.Size, self.Size)
        self.action = action

    def click_in_bound(self, point):
        return self.rect.collidepoint(point)

    def left_mouse_down_listener(self, point):
        if not self.click_in_bound(point):
            return
        if self.action:
            self.action(self)

    def draw(self):
        x = self.x * self.Size
        y = self.y * self.Size
        if not self.is_wall:
            pygame.draw.rect(self.root, WHITE, self.rect)
        else:
            pygame.draw.rect(self.root, BLACK,  self.rect)
        pygame.draw.rect(self.root, GRAY, self.rect, 2)
