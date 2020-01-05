


class UIElement:
    def __init__(self, text, width, height, colors, canvas):
        self.text = text
        self.width = width
        self.height = height
        self.colors = colors
        self.canvas = canvas
        self.selected = False

    def selected(self, is_selected):
        pass

    def render(self):
        pass

