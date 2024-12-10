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
add_wall_btn = Button((510, 8), (178, 50), "Add Wall", *btn_color_schema)
add_wall_btn.set_action(grid.set_wall)

gameOn = True
while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                point = pygame.mouse.get_pos()
                add_wall_btn.left_mouse_down_listener(point)
                grid.cell_click_listener(point)

    sc.fill(colors.GRAY)

    grid.draw_maze()
    add_wall_btn.update(sc)
    pygame.display.flip()
    clock.tick(60)
