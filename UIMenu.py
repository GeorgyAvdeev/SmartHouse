from UIElement import *
from MenuStack import *


class UIMenu(UIElement):
    def __init__(self, text, coords, width, height, colors, canvas, menu, menu_stack):
        super().__init__(text, coords, width, height, colors, canvas)
        self.menu = menu
        self.menuStack = menu_stack

    def do(self):
        self.menuStack.push(self.menu)

