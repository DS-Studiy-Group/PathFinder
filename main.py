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

    def mainloop(self):
        grid = self.grid
        sc = self.sc

        check_button_color_schema = (colors.BLACK, colors.GHOST, colors.BLACK, colors.LIME_GREEN)
        text_box_color_schema = (colors.BLACK, colors.GHOST)
        click_button_color_schema = (colors.BLACK, colors.ORANGE)

        titles = ["Add Wall", "Add Value", "Add Start", "Add End"]
        check_button_group = CheckButtonGroup(sc, (510, 8), (178, 50), titles, check_button_color_schema)
        actions = [grid.set_wall, grid.set_value, grid.set_start, grid.set_end]
        check_button_group.set_actions(*actions)

        value_txt = TextBox(sc, (510, 240), (178, 40), *text_box_color_schema)
        solve_btn = ClickButton(sc, (510, 298), (178, 50), "Solve", *click_button_color_schema)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        point = pygame.mouse.get_pos()

                        check_button_group.left_mouse_down_listener(point)
                        value_txt.left_mouse_down_listener(point)
                        solve_btn.left_mouse_down_listener(point)
                        grid.cell_click_listener(point)

                if event.type == pygame.KEYDOWN:
                    if value_txt.focused:
                        value_txt.key_down_listener(event.key)
                    else:
                        grid.cell_value(event.key)

            self.sc.fill(colors.GRAY)

            grid.draw_maze()

            check_button_group.update()
            value_txt.update()
            solve_btn.update()

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    mw = MainWindow()
    mw.mainloop()
