import random as rand
import sys
import time
from tkinter import *

#Tile class has attributes: coordinates, whether it is a mine, whether it is revealed and if there are neighbouring mines.
#A tile can be reset and revealed
class Tile:
    #A Tile of the game 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.reset()

    def reset(self):
        self.is_mine = False
        self.revealed = False
        self.neighbour_mines = 0

    def reveal(self):
        self.revealed = True
        return self.is_mine, self.neighbour_mines


class Grid:
    # A game grid, containing Tiles
    def __init__(self):
        self.height = 10
        self.width = 15
        self.mines = 20
        self.mines_remain = self.mines
        self.tiles_revealed = 0
        self.init_time = time.time()
        self.neighbours = self.populate_game()
        self.backing_grid = self.create_grid()
        
    def reset(self):
        for line in self.backing_grid:
            for tile in line:
                tile.reset()

    def populate_game(self):
        neighbours = dict()
        for row in range(self.height):
            for col in range(self.width):
                adjacent = list()
                #D O W N 
                if row+1 < self.height:
                    adjacent.append([row+1, col]) 
                #D O W N  L E F T
                if 0 <= row+1 < self.height and 0 <= col-1:
                    adjacent.append([row+1, col-1])
                #L E F T
                if col-1 >= 0:
                    adjacent.append([row, col-1])
                #T O P  L E F T
                if 0 <= row-1 and 0 <= col-1:
                    adjacent.append([row-1, col-1])
                #T O P
                if row-1 >= 0:
                    adjacent.append([row-1, col])
                #T O P  R I G H T
                if 0 <= row-1 and col+1 < self.width:
                    adjacent.append([row-1, col+1])
                #R I G H T
                if col+1 < self.width:
                    adjacent.append([row, col+1])
                #D O W N  R I G H T
                if row+1 < self.height and col+1 < self.width:
                    adjacent.append([row+1, col+1])
                neighbours[row, col] = adjacent
        return neighbours
    
    def generate_mines(self):
        mines = rand.sample([(i, j) for j in range (self.width) for i in range(self.height)], self.mines)
        for i, j in mines:
            self.backing_grid[i][j].is_mine = True
            for i2, j2 in self.neighbours[i, j]:
                self.backing_grid[i2][j2].neighbour_mines += 1

    def create_grid(self):
        backing_grid = [[Tile(i, j) for i in range(self.width)] for j in range(self.height)]
        return backing_grid

    def get_neighbours(self):
        return self.neighbours

    def get_grid(self):
        return self.backing_grid

    