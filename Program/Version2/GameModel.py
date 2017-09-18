import random as rand
import sys
import time
from tkinter import *

class GameModel:
    # A game grid, containing Tiles
    def __init__(self):
        self.height = 10
        self.width = 15
        self.size = self.width*self.height
        self.mine_count = 20
        self.init_time = time.time()
        self.neighbours = self.get_neighbours()
        self.backing_grid = self.get_grid()
        self.mines = self.generate_mines()

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
        mines = list()
        for i in range(self.size * self.mine_count):
            #generate coordinates for mines
            x = rand.randrange(0, self.size)
            y = rand.randrange(0, self.size)
            mines.append([x, y])
        return mines 

    def mine_exists(self, row, col):
        for mine in self.mines:
            if mine[0] == row and mine[1] == col:
                return True
        return False 

    def create_backing_grid(self):
        backing_grid = [[0 for col in range(self.width)] for row in range(self.height)]
        for row in range(self.height):
            for col in range (self.width):
                count = 0
                if self.mine_exists(row, col):
                    backing_grid[row][col] = 'B'
                else:
                    for neighbour in self.neighbours[row, col]:
                        if self.mine_exists(neighbour[0], neighbour[1]):
                            count += 1
                    backing_grid[row][col] = count
        return backing_grid

    def cascade_reveal(self, i, j):
        reveal = list()
        adjacent = self.neighbours[i, j]
        for neighbour in adjacent:
            if self.backing_grid[neighbour[0]][neighbour[1]] == 0:
                reveal.append(neighbour)

        while reveal:
            for cell in reveal:
                adjacent = self.neighbours[cell[0], cell[1]]
                if self.backing_grid[cell[0]][cell[1]] == 0:
                    # self.buttons[cell[0]][cell[1]].itemconfig(relief=SUNKEN, text='', background='pink', state='disabled')
                    self.backing_grid[cell[0]][cell[1]] = 's'
                for neighbour in adjacent:
                    if self.backing_grid[neighbour[0]][neighbour[1]] == 0:
                        reveal.append(neighbour)
                    elif self.backing_grid[neighbour[0]][neighbour[1]] == 1:
                        # self.buttons[neighbour[0]][neighbour[1]].itemconfig(relief=SUNKEN, text='1', background='pink', state='disabled')
                    elif self.backing_grid[neighbour[0]][neighbour[1]] == 2:
                        # self.buttons[neighbour[0]][neighbour[1]].itemconfig(relief=SUNKEN, text='2', background='pink', state='disabled')
                reveal.remove(cell)

    def get_neighbours(self):
        return self.neighbours

    def get_grid(self):
        return self.backing_grid

    