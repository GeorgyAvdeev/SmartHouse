from UIElement import *


class UIMenu(UIElement):
    def __init__(self, text, coords, width, height, colors, canvas, menu, menu_stack):
        super().__init__(text, coords, width, height, colors, canvas)
        self.menu = menu

    def do(self):
        //Реализовать переход на новое меню // menuStack
        pass

