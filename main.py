from tkinter import *
from UIElement import *
from Coords import *

selection_number = 0

def Up(event):
    global selection_number
    if selection_number >= 1:
        selection_number -= 1


def Down(event):
    global selection_number
    if selection_number < 2:
        selection_number += 1


window = Tk()

canvas = Canvas(window, width=400, height=300, bg='green')
UI1 = UIElement("temperature = 30°C", Coords(0, 0), 400, 100, "", canvas)

UI2 = UIElement("light on", Coords(0, 100), 400, 100, "", canvas)

UI3 = UIElement("settings", Coords(0, 200), 400, 100, "", canvas)

UI = [UI1, UI2, UI3]

canvas.pack()

window.bind('<Up>', Up)
window.bind('<Down>', Down)

while True:
    window.update()
    UI[selection_number].select(True)
    UI1.render()
    UI2.render()
    UI3.render()
    UI[selection_number].select(False)
