from pygame import Surface, Rect
from pygame.font import Font


class Button():
    font = Font("arial.ttf", 20)

    def __init__(self, pos, size, text, base_color, hovering_color):
        self.pos = pos
        self.size = size
        self.base_color, self.hovering_color = base_color, hovering_color
        self.color = base_color
        self.text = text

    def button_surface(self):
        surf = Surface(self.size)
        surf.fill(self.color)
        text_surf = self.font.render(self.text, True, self.base_color)
        text_rect = self.text.get_rect(center=self.pos)
        surf.blit(text_surf, text_rect)
        return surf

    def point_in_bound(self, point):
        pos = self.pos
        size = self.size
        rect = Rect(pos[0], pos[1], pos[0]+size[0], pos[1]+size[1])
        return rect.collidepoint(point)

    def update(self, screen):
        screen.blit(self.button_surface(), self.pos)


