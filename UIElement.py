from Coords import *


class UIElement:
    def __init__(self, text, coords, width, height, colors, canvas):
        self.text = text
        self.coords = coords
        self.width = width
        self.height = height
        self.colors = colors
        self.canvas = canvas
        self.selected = False
        self.id_text = 0
        self.id_rectangle = 0

    def select(self, is_selected):
        self.selected = is_selected
        pass

    def render(self):
        self.id_rectangle = self.canvas.create_rectangle(self.coords.x, self.coords.y,
                                                         self.coords.x + self.width,
                                                         self.coords.y + self.height,
                                                         outline="#FFE773",
                                                         fill="#FFE773" if self.selected else "#FFD300")
        center = self.get_center()
        self.id_text = self.canvas.create_text(center.x, center.y,
                                               fill='#A68900',
                                               font="Purisa",
                                               text=self.text)
        pass

    def get_center(self):
        x = self.coords.x + self.width / 2
        y = self.coords.y + self.height / 2
        return Coords(x, y)