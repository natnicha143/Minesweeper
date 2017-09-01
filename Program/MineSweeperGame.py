from tkinter import *
import sys
import random as rand
import MineSweeperModel as ms 
import GameView 

class Tile():
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.reset()

    def reset(self):
        self.mine = False
        self.uncovered = False
        self.mine_count = 0

    def reveal(self):
        self.uncovered = True
        return self.mine, self.mine_count

class Grid():
    def __init__(self):
        self.grid = ms.backing_grid

    def reset(self):
        for line in self.grid:
            for tile in line:
                tile.reset()
    
 
###Main

#Set paramters


grid = Grid()
grid.generate_mines()

## GUI
master = GameView.main_window()
flag, mine = GameView.images()
board = GameView.create_board(master, mine, flag)
top_frame = GameView.make_top_frame(master, grid, board)

mainloop()