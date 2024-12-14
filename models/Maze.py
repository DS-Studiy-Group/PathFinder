from enum import Enum

import pygame

from models.Cell import Cell
from utils.solution_finder import find_solution_subsets
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
        self.cells = [[Cell(root, x, y, self.cell_click) for x in range(cols)] for y in range(rows)]
        self.state = MazeState.NONE

        self.set_value_selected_cell: Cell | None = None

        self.start_position = (0, 0)
        self.end_position = (-1, -1)
        self.target = None

    def draw_maze(self):
        for row in self.cells:
            for cell in row:
                cell.draw()

        if self.state == MazeState.SET_VALUE and self.set_value_selected_cell is not None:
            self.set_value_selected_cell.draw_mask(colors.BLUE_HIGHLIGHT)

        start_cell = self.cells[self.start_position[1]][self.start_position[0]]
        pygame.draw.rect(self.root, colors.LIME_GREEN, start_cell.get_rect())

        end_cell = self.cells[self.end_position[1]][self.end_position[0]]
        pygame.draw.rect(self.root, colors.SOFT_RED, end_cell.get_rect())

    def set_target(self, target):
        self.target = int(target)

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
        for row in self.cells:
            for cell in row:
                if cell.click_in_bound(point):
                    cell.left_mouse_down_listener(point)
                    break
            else:
                continue
            break

    def cell_click(self, cell):
        if self.state == MazeState.NONE:
            return
        if self.state == MazeState.SET_WALL:
            if (cell.x, cell.y) != self.start_position \
                    and (cell.x, cell.y) != self.end_position:
                cell.is_wall = not cell.is_wall

        elif self.state == MazeState.SET_VALUE:
            self.set_value_selected_cell = cell

        elif self.state == MazeState.SET_START:
            if not cell.is_wall:
                self.start_position = cell.x, cell.y

        elif self.state == MazeState.SET_END:
            if not cell.is_wall:
                self.end_position = cell.x, cell.y

    def cell_value(self, key):
        if self.state == MazeState.NONE:
            pass
        if self.state == MazeState.SET_VALUE:
            if 48 <= key <= 57:
                self.set_value_selected_cell.add_char(chr(key))
            elif key == pygame.K_BACKSPACE:
                self.set_value_selected_cell.del_char()

    def solve_maze(self):
        value_cells = []
        for row in self.cells:
            for cell in row:
                if not cell.is_wall and cell.value != "":
                    value_cells.append(cell)

        results = find_solution_subsets(value_cells, self.target)
