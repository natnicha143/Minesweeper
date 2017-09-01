from tkinter import *
import sys
import random as rand
import MineSweeperModel as ms 
import GameView 

height = ms.height
width = ms.width

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
        self.backing_grid = [[Tile(i, j)   for j in range(width)]
                                    for i in range(height)]

    def reset(self):
        for line in self.backing_grid:
            for tile in line:
                tile.reset()

    def generate_mines():
        mines = list()
        for i in range(ms.size * ms.mines):
            #generate coordinates for mines
            x = rand.randrange(0, ms.size)
            y = rand.randrange(0, ms.size)
            mines.append([x, y])
        return mines
 
