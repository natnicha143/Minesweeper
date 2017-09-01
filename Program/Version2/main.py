
import sys
import MineSweeperModel as ms
import GameView
import GameModel as gm
from tkinter import *
# Set parameters if given ######################################################
gm.set_parameters(sys.argv[1:])

# Initialisation of the data ###################################################
GRID = ms.Grid()
GRID.add_bombs()

# Creation of the GUI ##########################################################
window = GameView.create_main_window()
flag, mine = GameView.create_images()
BOARD = GameView.create_board(window, GRID, flag, mine)
top_frame = GameView.create_top_frame(window, GRID, BOARD)

mainloop()
