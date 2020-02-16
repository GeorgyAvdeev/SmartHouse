from UIElement import *


class UIInformation(UIElement):
    def __init__(self, text, coords, width, height, colors, canvas):
        super().__init__(text, coords, width, height, colors, canvas)
        self.pattern_text = text

    def render(self):
        temperature = 0 #get_temperature()
        self.text = self.pattern_text + str(temperature)
        super().render()