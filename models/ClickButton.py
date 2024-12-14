from pygame import Surface, font

font.init()


class ClickButton:
    btn_font = font.Font("resources/fonts/Quicksand-Regular.ttf", 20)

    def __init__(self,
                 root,
                 pos, size,
                 text,
                 base_fore_color,
                 base_back_color,
                 ):

        self.root = root
        self.pos = pos
        self.size = size
        self.text = text

        self.base_back_color = base_back_color,
        self.base_fore_color = base_fore_color

        self.action = None

    def button_surface(self):

        surf = Surface(self.size)
        surf.fill(self.base_back_color)
        text_surf = self.btn_font.render(self.text, True, self.base_fore_color)
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
            if self.action is not None:
                self.action()

    def set_action(self, func):
        self.action = func
