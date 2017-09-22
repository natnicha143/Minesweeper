import sys
from GameModel import GameModel
from SquareView import Square
from BoardController import BoardController
from MainMenu import MainMenu
from tkinter import *

#Main handles creating GUI, initialises data and calls mainloop
class MineSweeper:
    def __init__(self):

        #create main window
        self.root = Tk()
        self.root.title("Minesweeper")
        self.root.resizable(False, False)
        self.mainmenu = MainMenu(self.root)
        self.root.mainloop()
        self.height = self.mainmenu.height
        self.width = self.mainmenu.width
        self.mines = self.mainmenu.mines
        print(self.width, self.height)
        self.model = GameModel(self.height, self.width, self.mines)
        self.controller = BoardController(self.model)
        self.view = Square(self.root, self.controller, self.model, self.height, self.width)
        self.root.mainloop()
    
MineSweeper()

