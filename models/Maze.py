from enum import Enum

import pygame

from models.Cell import Cell
from resources import colors


class MazeState(Enum):
    NONE = 0
    SET_WALL = 1
    SET_VALUE = 2
    SET_START = 3
    SET_END = 4


class Maze:
    def __init__(self, root, cols, rows):
        self.root = root
        self.cols = cols
        self.rows = rows
        self.maze = [[Cell(root, x, y, self.cell_click) for x in range(cols)] for y in range(rows)]
        self.state = MazeState.NONE
        self.start_position = (0, 0)
        self.end_position = (-1, -1)

    def draw_maze(self):
        for row in self.maze:
            for cell in row:
                cell.draw()

        start_cell = self.maze[self.start_position[0]][self.start_position[1]]
        pygame.draw.rect(self.root, colors.LIME_GREEN, start_cell.rect)

        end_cell = self.maze[self.end_position[0]][self.end_position[1]]
        pygame.draw.rect(self.root, colors.SOFT_RED, end_cell.rect)



    def set_wall(self, alt):
        if alt:
            self.state = MazeState.SET_WALL
            return
        self.state = MazeState.NONE

    def set_value(self, alt):
        if alt:
            self.state = MazeState.SET_VALUE
            return
        self.state = MazeState.NONE

    def set_start(self, alt):
        if alt:
            self.state = MazeState.SET_START
            return
        self.state = MazeState.NONE

    def set_end(self, alt):
        self.state = MazeState.SET_END
        if alt:
            self.state = MazeState.SET_END
            return
        self.state = MazeState.NONE

    def cell_click_listener(self, point):
        for row in self.maze:
            for cell in row:
                if cell.click_in_bound(point):
                    cell.left_mouse_down_listener(point)
                    break
            else: continue
            break

    def cell_click(self, cell):
        if self.state == MazeState.NONE:
            return
        if self.state == MazeState.SET_WALL:
            if (cell.x, cell.y) != self.start_position \
                    and (cell.x, cell.y) != self.end_position:
                cell.is_wall = not cell.is_wall

        if self.state == MazeState.SET_VALUE:
            pass
