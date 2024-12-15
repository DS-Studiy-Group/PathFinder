from enum import Enum
from random import shuffle

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

    def get_cell(self, x, y):
        return self.cells[y][x]

    def get_next_cell(self, cell, vis, wanted_value_cells):
        directions = [(1, 0), (0, -1), (0, 1), (-1, 0)]
        for d in directions:
            next_x, next_y = cell.x + d[0], cell.y + d[1]
            if next_x < 0 or next_y < 0:
                continue
            try:
                next_cell = self.get_cell(next_x, next_y)
            except IndexError as _:
                continue

            if not next_cell.is_wall and next_cell not in vis:
                if next_cell.value != "" and (next_cell in wanted_value_cells):
                    vis.add(next_cell)
                    return next_cell
                if next_cell.value == "":
                    vis.add(next_cell)
                    return next_cell

        return None

    def dfs(self, start_cell, target_cells, wanted_value_cells):
        visited = {start_cell}
        stack = [start_cell]
        while stack:
            next_cell = next_cell = self.get_next_cell(stack[-1], visited, wanted_value_cells)
            if next_cell is None:
                stack.pop()
                continue

            else:
                stack.append(next_cell)
                if next_cell in target_cells:
                    break
        if not stack:
            return False, []
        else:
            return True, stack

    def reset_branches(self):
        for row in self.cells:
            for cell in row:
                cell.branches = []

    def solve_maze(self):
        value_cells = []
        for row in self.cells:
            for cell in row:
                if not cell.is_wall and cell.value != "":
                    value_cells.append(cell)

        results = find_solution_subsets(value_cells, self.target)

        for result in results:
            start_cell = self.get_cell(*self.start_position)
            end_cell = self.get_cell(*self.end_position)

            ok, dfs_solution = self.dfs(start_cell, {end_cell}, result)

            if not ok:
                continue

            dfs_solution_set = set(dfs_solution)

            ok = True
            for cell in result:
                if cell in dfs_solution_set:
                    continue

                else:
                    ok, branch_dfs_solution = self.dfs(cell, dfs_solution_set, result)
                    if not ok:
                        break

                    branch_dfs_solution[-1].branches.append(branch_dfs_solution)
                    for c in branch_dfs_solution:
                        dfs_solution_set.add(c)

            if not ok:
                self.reset_branches()
                continue

            return dfs_solution

        return None

