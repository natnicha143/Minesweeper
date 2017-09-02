
import sys
import MineSweeperModel as ms
import GameView
import GameModel as gm
import ButtonController as ButtonController
from tkinter import *
#Main handles creating GUI, initialises data and calls mainloop
gm.set_parameters(sys.argv[1:])

GRID = ms.Grid()
GRID.generate_mines()

self.controller = ButtonController

window = GameView.create_main_window()
flag, mine = GameView.create_images()
BOARD = GameView.create_board(window, GRID, flag, mine)
top_frame = GameView.create_top_frame(window, GRID, BOARD)

mainloop()
