import pygame
from resources.colors import GRAY, WHITE


class Cell:
    Size = 50
    Margin = 1

    def __init__(self, root, x, y):
        self.root = root
        self.x = x
        self.y = y
        self.is_wall = False
        self.is_temp_wall = False
        self.visited = False

    def draw(self):
        x = self.x * self.Size
        y = self.y * self.Size
        pygame.draw.rect(self.root, WHITE, (x, y, self.Size, self.Size))
        pygame.draw.rect(self.root, GRAY, (x, y, self.Size, self.Size), 2)
