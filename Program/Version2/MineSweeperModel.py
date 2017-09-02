import random as rand
import sys
from tkinter import *
import GameView
import time

HEIGHT = 10
WIDTH = 15
SIZE = HEIGHT * WIDTH
MINES = 20
REMAINING_MINES = MINES
TILES_REVEALED = 0
INIT_TIME = time.time()


#Tile class has attributes: coordinates, whether it is a mine, whether it is revealed and if there are neighbouring mines.
#A tile can be reset and revealed
class Tile():
    """ A Tile of the game """
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
        return (self.is_mine, self.neighbour_mines)

#A grid of tiles
class Grid():
    """ A game grid, containing Tiles """
    def __init__(self):
        self.buttons = [[Tile(i, j) for i in range(WIDTH)] for j in range(HEIGHT)]

    def reset(self):
        for line in self.buttons:
            for sq in line:
                sq.reset()

    def populate_game(self):
        neighbours = dict()
        for row in range(HEIGHT):
            for col in range(WIDTH):
                adjacent = list()
                #D O W N 
                if row+1 < HEIGHT:
                    adjacent.append([row+1, col]) 
                #D O W N  L E F T
                if 0 <= row+1 < HEIGHT and 0 <= col-1:
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
                if 0 <= row-1 and col+1 < WIDTH:
                    adjacent.append([row-1, col+1])
                #R I G H T
                if col+1 < WIDTH:
                    adjacent.append([row, col+1])
                #D O W N  R I G H T
                if row+1 < HEIGHT and col+1 < WIDTH:
                    adjacent.append([row+1, col+1])
                neighbours[row, col] = adjacent
        return neighbours

    def generate_mines(self):
        mines = rand.sample([(i, j) for j in range (WIDTH) for i in range(HEIGHT)], MINES)
        for i, j in mines:
            self.buttons[i][j].is_mine = True
            for i2, j2 in neighbours[i, j]:
                self.buttons[i2][j2].neighbour_mines += 1

    def set_parameters(self, argv):
        # if there's not 3 args
        if len(argv) != 3:
            if len(argv) != 0:
                print("Warning : Invalid parameters")
                print("Need 3 arguments (height, WIDTH, mines)")
            return

        # if they aren't ints
        try:
            height = int(argv[0])
            WIDTH = int(argv[1])
            mines = int(argv[2])
        except ValueError:
            print("Warning : Invalid parameters")
            print("Arguments aren't ints")
            return

        # if constraints aren't respected
        if  height <= 0 or WIDTH <= 0 or mines <= 0 or mines >= height*WIDTH:
            print("Warning : Invalid parameters")
            print("Can't create game with these values")
            return

        HEIGHT = height
        WIDTH = WIDTH
        MINES = mines
        REMAINING_MINES = mines

