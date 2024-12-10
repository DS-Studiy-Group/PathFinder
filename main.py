import pygame
from pygame import font

from models.Button import Button
from models.Cell import Cell
from models.Maze import Maze
from resources import colors

Rows, Cols = 10, 10
width, height = 700, Rows * Cell.Size + 2
clock = pygame.time.Clock()

pygame.init()
font.init()

sc = pygame.display.set_mode((width, height))
pygame.display.set_caption("AD Maze Generator")

grid = Maze(sc, cols=Cols, rows=Rows)

btn_color_schema = (colors.BLACK, colors.GHOST, colors.WHITE, colors.LIME_GREEN)
btn1 = Button((510, 8), (178, 50), "test", *btn_color_schema)

gameOn = True
while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                btn1.left_mouse_down(pygame.mouse.get_pos())

    sc.fill(colors.GRAY)

    grid.draw_maze()
    btn1.update(sc)
    pygame.display.flip()
    clock.tick(60)
