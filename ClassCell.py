import pygame
import random

Tile = 20
margin = 1
width , height = 1000 , 600
Rows , Cols = height // Tile , width // Tile

pygame.init()
sc = pygame.display.set_mode((width, height))
pygame.display.set_caption("AD Maze Generator")

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = {"up": True, "down": True, "left": True, "right": True}
        self.visited = False
    def draw(self):
        x = self.x * Tile
        y = self.y * Tile
        if self.visited:
            pygame.draw.rect(sc, pygame.Color('#a9237d'), (x, y, Tile, Tile))
        if self.walls["up"]:
            pygame.draw.line(sc, pygame.Color('#060105'), (x, y), (x + Tile, y), 2)
        if self.walls["right"]:
            pygame.draw.line(sc, pygame.Color('#060105'), (x + Tile, y), (x + Tile, y + Tile), 2)
        if self.walls["down"]:
            pygame.draw.line(sc, pygame.Color('#060105'), (x + Tile, y + Tile), (x, y + Tile), 2)
        if self.walls["left"]:
            pygame.draw.line(sc, pygame.Color('#060105'), (x, y + Tile), (x, y), 2)


    def check_neighbors(self, grid):
        neighbors = []
        directions = [
            (0, -1, "Up", "down"),
            (0, 1, "down", "Up"),
            (-1, 0, "left", "right"),
            (1, 0, "right", "left"),
        ]
        for dx, dy, wall1, wall2 in directions:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < Cols and 0 <= ny < Rows:
                neighbor = grid[ny * Cols + nx]
                if not neighbor.visited:
                    neighbors.append((neighbor, wall1, wall2))
        return random.choice(neighbors) if neighbors else None
