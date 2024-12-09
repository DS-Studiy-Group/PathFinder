import pygame
from pygame import font

from Button_class import Button
from ClassCell import Cell
from resources import colors

Rows, Cols = 10, 10
width, height = 700, Rows * Cell.Size + 2

pygame.init()
font.init()

sc = pygame.display.set_mode((width, height))
pygame.display.set_caption("AD Maze Generator")

grid = [[Cell(sc, x, y) for x in range(Cols)] for y in range(Rows)]

btn1 = Button((510, 8), (178, 50), "test", colors.BLACK, colors.GHOST, colors.WHITE, colors.LIME_GREEN)

gameOn = True
while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                btn1.left_mouse_down(pygame.mouse.get_pos())

    sc.fill(colors.GRAY)

    for row in grid:
        for cell in row:
            cell.draw()

    btn1.update(sc)
    pygame.display.flip()
