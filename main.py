import pygame
from pygame import font

from models.Button import Button
from models.Cell import Cell
from models.Maze import Maze
from models.TextBox import TextBox
from resources import colors

Rows, Cols = 10, 10
width, height = 700, Rows * Cell.Size + 2
clock = pygame.time.Clock()

pygame.init()
font.init()

sc = pygame.display.set_mode((width, height))
pygame.display.set_caption("AD Maze Generator")

grid = Maze(sc, cols=Cols, rows=Rows)

btn_color_schema = (colors.BLACK, colors.GHOST, colors.BLACK, colors.LIME_GREEN)

add_wall_btn = Button(sc, (510, 8), (178, 50), "Add Wall", *btn_color_schema)
add_wall_btn.set_action(grid.set_wall)

add_value_btn = Button(sc, (510, 66), (178, 50), "Add Value", *btn_color_schema)
add_value_btn.set_action(grid.set_value)

add_start_btn = Button(sc, (510, 124), (178, 50), "Add Start", *btn_color_schema)
add_start_btn.set_action(grid.set_start)

add_end_btn = Button(sc, (510, 182), (178, 50), "Add End", *btn_color_schema)
add_end_btn.set_action(grid.set_end)

value_txt = TextBox(sc, (510, 240), (178, 50), *btn_color_schema[:2])

gameOn = True
while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                point = pygame.mouse.get_pos()

                add_wall_btn.left_mouse_down_listener(point)
                add_value_btn.left_mouse_down_listener(point)
                add_start_btn.left_mouse_down_listener(point)
                add_end_btn.left_mouse_down_listener(point)
                value_txt.left_mouse_down_listener(point)
                grid.cell_click_listener(point)

        if event.type == pygame.KEYDOWN:
            if value_txt.focused:
                value_txt.key_down_listener(event.key)
            else:
                grid.cell_value(event.key)

    sc.fill(colors.GRAY)

    grid.draw_maze()

    add_wall_btn.update()
    add_value_btn.update()
    add_start_btn.update()
    add_end_btn.update()
    value_txt.update()

    pygame.display.flip()
    clock.tick(60)
