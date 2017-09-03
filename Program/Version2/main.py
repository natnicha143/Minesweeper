import sys
import MineSweeperModel as ms
import GameView as v
from tkinter import *
#Main handles creating GUI, initialises data and calls mainloop
# set_parameters(sys.argv[1:])

GRID = ms.Grid()
GRID.generate_mines()

window = view.create_main_window()
flag, mine = view.create_images()
BOARD = view.create_board(window, GRID, flag, mine)
top_frame = view.create_top_frame(window, GRID, BOARD)

mainloop()
