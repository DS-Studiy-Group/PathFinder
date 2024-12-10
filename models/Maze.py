from enum import Enum

from models.Cell import Cell


class MazeState(Enum):
    NONE = 0
    SET_WALL = 1
    SET_VALUE = 2
    SET_START = 3
    SET_END = 4


class Maze:
    def __init__(self, root, cols, rows):
        self.cols = cols
        self.rows = rows
        self.maze = [[Cell(root, x, y) for x in range(cols)] for y in range(rows)]
        self.state = MazeState.NONE

    def draw_maze(self):
        for row in self.maze:
            for cell in row:
                cell.draw()

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

    def cell_click(self, cell):
        if self.state == MazeState.NONE:
            return
        if self.state == MazeState.SET_WALL:
            cell.is_wall = not cell.is_wall

        if self.state == MazeState.SET_VALUE:
            pass
