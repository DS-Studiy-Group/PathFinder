import pygame

from ClassCell import Cell
from resources.colors import GRAY

Rows , Cols = 10 , 10
width , height = 700 , Cols * Cell.Size

pygame.init()
sc = pygame.display.set_mode((width, height))
pygame.display.set_caption("AD Maze Generator")

grid = [[Cell(sc, x, y) for x in range(Cols)] for y in range(Rows)]

gameOn = True
while gameOn:
    sc.fill(GRAY)
    for row in grid:
        for cell in row:
            cell.draw()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False

pygame.quit()
