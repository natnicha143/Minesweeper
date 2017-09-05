import sys
from GameModel import Grid
from GameView import SquareView
from TopMenu import TopMenu
from BoardController import BoardController
from TopMenu import TopMenu
from MainMenu import MainMenu
from tkinter import *
#Main handles creating GUI, initialises data and calls mainloop

class MineSweeper:
    def __init__(self):
        #create main window
        self.root = Tk()
        self.root.title("Mine Sweeper")
        self.root["bg"] = "black"
        self.root.resizable(width=False, height=False)
        self.model = Grid()
        self.controller = BoardController(self.model)
        self.view = SquareView(self.controller, self.model)
        self.mainmenu = MainMenu()
        self.topmenu = TopMenu(self.root, self.model, self.view, self.board)
        self.root.mainloop()

MineSweeper()

