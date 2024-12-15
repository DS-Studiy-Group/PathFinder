from pygame import font, Surface, Rect
from resources import colors

font.init()


class CheckButton():
    btn_font = font.Font("resources/fonts/Quicksand-Regular.ttf", 20)

    def __init__(self,
                 root,
                 pos, size,
                 text,
                 base_fore_color,
                 base_back_color,
                 alt_fore_color,
                 alt_back_color,
                 ):

        self.root = root
        self.pos = pos
        self.size = size
        self.text = text

        self.base_back_color = base_back_color,
        self.alt_back_color = alt_back_color
        self.base_fore_color = base_fore_color
        self.alt_fore_color = alt_fore_color

        self.is_alt = False
        self.action = None

    def button_surface(self):
        fore_color = ()
        back_color = ()
        if self.is_alt:
            fore_color = self.alt_fore_color
            back_color = self.alt_back_color
        else:
            fore_color = self.base_fore_color
            back_color = self.base_back_color

        surf = Surface(self.size)
        surf.fill(back_color)
        text_surf = self.btn_font.render(self.text, True, fore_color)
        text_rect = text_surf.get_rect(center=surf.get_rect().center)
        surf.blit(text_surf, text_rect)
        return surf

    def point_in_bound(self, point):
        pos = self.pos
        size = self.size
        rect = (pos[0], pos[1], pos[0] + size[0], pos[1] + size[1])

        return rect[0] <= point[0] <= rect[2] and rect[1] <= point[1] <= rect[3]

    def update(self):
        self.root.blit(self.button_surface(), self.pos)

    def left_mouse_down_listener(self, point):
        if self.point_in_bound(point):
            self.is_alt = not self.is_alt
            if self.action is not None:
                self.action(self.is_alt)

    def set_action(self, func):
        self.action = func


class CheckButtonGroup:
    def __init__(self, root, pos, size, titles, color_schema):
        self.buttons = []
        self.pos = pos
        c_pos = pos
        for title in titles:
            button = CheckButton(root, c_pos, size, title, *color_schema)
            self.buttons.append(button)
            c_pos = (c_pos[0], c_pos[1]+58)

    def set_actions(self, *funcs):
        for i in range(len(funcs)):
            self.buttons[i].set_action(funcs[i])

    def update(self):
        for button in self.buttons:
            button.update()

    def left_mouse_down_listener(self, point):
        for i in range(len(self.buttons)):
            btn = self.buttons[i]

            if btn.point_in_bound(point):
                btn.is_alt = not btn.is_alt
                for j in range(len(self.buttons)):
                    if i == j:
                        continue

                    self.buttons[j].is_alt = False

                if btn.action is not None:
                    btn.action(btn.is_alt)

                break





