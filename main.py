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
UI1 = UIElement("temperature = 30°C", Coords(0, 0), 400, 100, "", canvas)

UI2 = UIElement("light on", Coords(0, 100), 400, 100, "", canvas)

UI3 = UIElement("settings", Coords(0, 200), 400, 100, "", canvas)

UI4 = UIElement("4", Coords(0, 300), 400, 100, "", canvas)

UI5 = UIElement("5", Coords(0, 400), 400, 100, "", canvas)

UI6 = UIElement("6", Coords(0, 500), 400, 100, "", canvas)

UI7 = UIElement("7", Coords(0, 600), 400, 100, "", canvas)

UI8 = UIElement("8", Coords(0, 700), 400, 100, "", canvas)

UI9 = UIElement("9", Coords(0, 800), 400, 100, "", canvas)

UI10 = UIElement("10", Coords(0, 900), 400, 100, "", canvas)

UI = [UI1, UI2, UI3, UI4, UI5, UI6, UI7, UI8, UI9, UI10]

canvas.pack()

window.bind('<Up>', Up)
window.bind('<Down>', Down)

while True:
    window.update()
    UI[selection_number].select(True)
    UI1.render()
    UI2.render()
    UI3.render()
    UI4.render()
    UI5.render()
    UI6.render()
    UI7.render()
    UI8.render()
    UI9.render()
    UI10.render()
    UI[selection_number].select(False)
