from tkinter import *
from UIElement import *
from Coords import *

window = Tk()

canvas = Canvas(window, width=400, height=300, bg='green')
UI1 = UIElement("temperature = 30°C", Coords(0, 0), 400, 100, "", canvas)
UI1.select(True)
UI2 = UIElement("light on", Coords(0, 100), 400, 100, "", canvas)
UI2.select(True)
UI3 = UIElement("settings", Coords(0, 200), 400, 100, "", canvas)
UI3.select(True)

canvas.pack()
while True:
    window.update()
    UI1.render()
    UI2.render()
    UI3.render()

