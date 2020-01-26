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
    if selection_number < 9:
        selection_number += 1


window = Tk()

canvas = Canvas(window, width=400, height=1000, bg='green')
UI = []

UI.append(UIElement("temperature = 30°C", Coords(0, 0), 400, 100, "", canvas))

UI.append(UIElement("light on", Coords(0, 100), 400, 100, "", canvas))

UI.append(UIElement("settings", Coords(0, 200), 400, 100, "", canvas))

UI.append(UIElement("4", Coords(0, 300), 400, 100, "", canvas))

UI.append(UIElement("5", Coords(0, 400), 400, 100, "", canvas))

UI.append(UIElement("6", Coords(0, 500), 400, 100, "", canvas))

UI.append(UIElement("7", Coords(0, 600), 400, 100, "", canvas))

UI.append(UIElement("8", Coords(0, 700), 400, 100, "", canvas))

UI.append(UIElement("9", Coords(0, 800), 400, 100, "", canvas))

UI.append(UIElement("10", Coords(0, 900), 400, 100, "", canvas))



canvas.pack()

window.bind('<Up>', Up)
window.bind('<Down>', Down)

while True:
    window.update()
    UI[selection_number].select(True)
    for i in UI:
        i.render()
    UI[selection_number].select(False)
