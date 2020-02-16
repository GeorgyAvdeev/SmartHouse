from tkinter import *
#from UIElement import *
from Coords import *
from UIInformation import *
from UIButton import *
from UIMenu import *
from MenuStack import *


def Up(event):
    global menuStack
    if menuStack.get_position() > 0:
        menuStack.set_position(menuStack.get_position() - 1)


def Down(event):
    global menuStack
    if menuStack.get_position() < len(menuStack.get_menu()) - 1:
        menuStack.set_position(menuStack.get_position() + 1)

def Enter(event):
    menuStack.get_menu()[menuStack.get_position()].do()

def Escape(event):
    menuStack.pop()


window = Tk()

canvas = Canvas(window, width=800, height=1000, bg='green')

first_menu = []
menu_settings = []
menuStack = MenuStack(first_menu)

first_menu.append(UIInformation("temperature °C ", Coords(0, 0), 400, 100, "", canvas))
first_menu.append(UIButton("light on", Coords(0, 100), 400, 100, "", canvas, lambda : print('light on')))
first_menu.append(UIMenu("settings", Coords(0, 200), 400, 100, "", canvas, menu_settings, menuStack)) #//uimenu (4,5,6)
first_menu.append(UIElement("4", Coords(0, 300), 400, 100, "", canvas))
first_menu.append(UIElement("5", Coords(0, 400), 400, 100, "", canvas)) #// uimenu (1,2,3)
first_menu.append(UIElement("6", Coords(400, 100), 400, 100, "", canvas))
first_menu.append(UIElement("7", Coords(400, 200), 400, 100, "", canvas))
first_menu.append(UIElement("9", Coords(400, 300), 400, 100, "", canvas))
first_menu.append(UIElement("10", Coords(400, 400), 400, 100, "", canvas))


menu_settings.append(UIInformation("11", Coords(0, 0), 400, 100, "", canvas))
menu_settings.append(UIButton("12", Coords(0, 100), 400, 100, "", canvas, lambda : print('light on')))
menu_settings.append(UIElement("13", Coords(0, 200), 400, 100, "", canvas)) #//uimenu (4,5,6)
menu_settings.append(UIElement("14", Coords(0, 300), 400, 100, "", canvas))
menu_settings.append(UIElement("15", Coords(0, 400), 400, 100, "", canvas)) #// uimenu (1,2,3)
menu_settings.append(UIElement("16", Coords(400, 100), 400, 100, "", canvas))
menu_settings.append(UIElement("17", Coords(400, 200), 400, 100, "", canvas))
menu_settings.append(UIElement("18", Coords(400, 300), 400, 100, "", canvas))
menu_settings.append(UIElement("19", Coords(400, 400), 400, 100, "", canvas))



canvas.pack()

window.bind('<Up>', Up)
window.bind('<Down>', Down)
window.bind('<Return>', Enter)
window.bind('<Escape>', Escape)
while True:
    window.update()
    menuStack.get_menu()[menuStack.get_position()].select(True)
    for i in menuStack.get_menu():
        i.render()
    menuStack.get_menu()[menuStack.get_position()].select(False)
