from tkinter import *
#from UIElement import *
from Coords import *
from UIInformation import *
from UIButton import *
from MenuStack import *


def Up(event):
    global menuStack
    if menuStack.get_position() > 0:
        menuStack.set_position(menuStack.get_position() - 1)


def Down(event):
    global menuStack
    if menuStack.get_position() < len(menuStack.get_menu()) - 1:
        menuStack.set_position(menuStack.get_position() + 1)


window = Tk()

canvas = Canvas(window, width=800, height=1000, bg='green')

first_menu = []
first_menu.append(UIInformation("temperature °C ", Coords(0, 0), 400, 100, "", canvas))
first_menu.append(UIButton("light on", Coords(0, 100), 400, 100, "", canvas, lambda : print('light on')))
first_menu.append(UIElement("settings", Coords(0, 200), 400, 100, "", canvas)) //uimenu (4,5,6)
first_menu.append(UIElement("4", Coords(0, 300), 400, 100, "", canvas))
first_menu.append(UIElement("5", Coords(0, 400), 400, 100, "", canvas)) // uimenu (1,2,3)
first_menu.append(UIElement("6", Coords(400, 100), 400, 100, "", canvas))
first_menu.append(UIElement("7", Coords(400, 200), 400, 100, "", canvas))
first_menu.append(UIElement("9", Coords(400, 300), 400, 100, "", canvas))
first_menu.append(UIElement("10", Coords(400, 400), 400, 100, "", canvas))

menuStack = MenuStack(first_menu)

canvas.pack()

window.bind('<Up>', Up)
window.bind('<Down>', Down)

while True:
    window.update()
    menuStack.get_menu()[menuStack.get_position()].select(True)
    for i in menuStack.get_menu():
        i.render()
    menuStack.get_menu()[menuStack.get_position()].select(False)
