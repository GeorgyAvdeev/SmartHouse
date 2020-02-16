from UIElement import *


class UIButton(UIElement):
    def __init__(self, text, coords, width, height, colors, canvas, action):
        super().__init__(text, coords, width, height, colors, canvas)
        self.action = action

    def do(self):
        self.action()
