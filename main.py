import pygame
from pygame import font

from models.ClickButton import ClickButton
from models.CheckButton import CheckButton, CheckButtonGroup
from models.Cell import Cell
from models.Maze import Maze
from models.TextBox import TextBox
from resources import colors

pygame.init()


class MainWindow:
    ROWS, COLS = 10, 10
    WIDTH, HEIGHT = 700, ROWS * Cell.Size + 20

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.sc = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.grid = Maze(self.sc, cols=self.COLS, rows=self.ROWS)
        self.running = True

        self.animate = False
        self.animator = None
        self.solution = None

        check_button_color_schema = (colors.BLACK, colors.GHOST, colors.BLACK, colors.LIME_GREEN)
        text_box_color_schema = (colors.BLACK, colors.GHOST)
        click_button_color_schema = (colors.BLACK, colors.ORANGE)

        titles = ["Add Wall", "Add Value", "Add Start", "Add End"]
        self.check_button_group = CheckButtonGroup(self.sc, (510, 8), (178, 50), titles, check_button_color_schema)
        actions = [self.grid.set_wall, self.grid.set_value, self.grid.set_start, self.grid.set_end]
        self.check_button_group.set_actions(*actions)

        self.value_txt = TextBox(self.sc, (510, 240), (178, 40), *text_box_color_schema)

        self.solve_btn = ClickButton(self.sc, (510, 298), (178, 50), "Solve", *click_button_color_schema)
        self.solve_btn.set_action(self.solve_maze)

        self.reanimate_btn = ClickButton(self.sc, (510, 356), (178, 50), "Reanimate", *click_button_color_schema)
        self.reanimate_btn.set_action(self.reanimate_maze)

        self.clear_btn = ClickButton(self.sc, (510, 414), (178, 50), "Clear", *click_button_color_schema)
        self.clear_btn.set_action(self.clear_maze)

    def solve_maze(self):
        try:
            self.grid.set_target(self.value_txt.text)
        except ValueError as _:
            print("empty text_box")
            return

        self.solution = self.grid.solve_maze()
        if self.solution is None:
            print("no solution found")

        else:
            self.animate = True
            self.animator = self.animate_main_solution()

    def reanimate_maze(self):
        if self.animate:
            self.animator = self.animate_main_solution()

    def clear_maze(self):
        self.animate = False
        self.animator = None
        self.solution = None

        for row in self.grid.cells:
            for cell in row:
                cell.reset()

    def draw_circle(self, cell: Cell):
        cell.color = colors.YELLOW
        cell_center = (cell.gx + Cell.Size / 2, cell.gy + Cell.Size / 2)
        pygame.draw.circle(self.sc, colors.SKY_BLUE, cell_center, (Cell.Size / 2.0))

    def animate_main_solution(self):
        if self.animate:

            for cell in self.solution:
                self.draw_circle(cell)
                yield
                if cell.branches:
                    for branch in cell.branches:
                        for _ in self.animate_branch_solution(branch):
                            yield

            while True:
                self.draw_circle(self.solution[-1])
                yield

    def animate_branch_solution(self, branch: list):
        b = branch[::-1]
        # print("branch", [(c.x, c.y) for c in branch])
        for cell in b[1:]:
            self.draw_circle(cell)
            yield

            if cell.branches:
                # print("x, y", cell.x, cell.y)
                for sub_branch in cell.branches:
                    for _ in self.animate_branch_solution(sub_branch):
                        yield
        for cell in branch:
            self.draw_circle(cell)
            yield

    def mainloop(self):


        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        point = pygame.mouse.get_pos()

                        self.check_button_group.left_mouse_down_listener(point)
                        self.value_txt.left_mouse_down_listener(point)
                        self.solve_btn.left_mouse_down_listener(point)
                        self.reanimate_btn.left_mouse_down_listener(point)
                        self.clear_btn.left_mouse_down_listener(point)
                        self.grid.cell_click_listener(point)

                if event.type == pygame.KEYDOWN:
                    if self.value_txt.focused:
                        self.value_txt.key_down_listener(event.key)
                    else:
                        self.grid.cell_value(event.key)

            self.sc.fill(colors.GRAY)

            self.grid.draw_maze()

            self.check_button_group.update()
            self.value_txt.update()
            self.solve_btn.update()
            self.reanimate_btn.update()
            self.clear_btn.update()

            if self.animate:
                self.animator.__next__()

            pygame.display.flip()
            self.clock.tick(10)


if __name__ == "__main__":
    mw = MainWindow()
    mw.mainloop()
