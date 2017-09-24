import random as rand
from tkinter import *

class GameModel:
    # A game grid, containing Tiles
    def __init__(self, height, width, mines):
        self.height = height
        self.width = width
        self.size = self.width * self.height
        self.mine_count = mines
        self.neighbours = self.populate_game()
        self.mines = self.generate_mines()
        self.backing_grid = self.create_backing_grid()
        self.game_over = False
        self.toggled = [[False for i in range(self.width)]for j in range(self.height)]
        self.flagged = [[False for i in range(self.size)]for j in range(self.height)]

    # function that populates the board and returns a dictionary of each cell's adjacent cells
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
    
    # function that populates the grid with mines, returns a list of mines
    def generate_mines(self):
        mines = list()
        for i in range(self.size * self.mine_count):
            #generate coordinates for mines
            x = rand.randrange(0, self.size)
            y = rand.randrange(0, self.size)
            mines.append([x, y])
        return mines 

    # function that returns a boolean: True if mine exists in current position, False if otherwise
    def mine_exists(self, row, col):
        for mine in self.mines:
            if mine[0] == row and mine[1] == col:
                return True
        return False 

    # function that creates the backing board for the game, assigns a number or letter depending on its value
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

    # called when an empty cell of value 0 is clicked, will reveal all surrounding cells if the condition is met
    def cascade_reveal(self, i, j):
        reveal = list()
        adjacent = self.neighbours[i, j]
        for neighbour in adjacent:
            if self.backing_grid[neighbour[0]][neighbour[1]] == 0:
                reveal.append(neighbour)
                self.toggled[neighbour[0]][neighbour[1]] = True                

        while reveal:
            for cell in reveal:
                adjacent = self.neighbours[cell[0], cell[1]]
                if self.backing_grid[cell[0]][cell[1]] == 0:
                    self.toggled[cell[0]][cell[1]] = True
                    self.backing_grid[cell[0]][cell[1]] = 's'
                for neighbour in adjacent:
                    if self.backing_grid[neighbour[0]][neighbour[1]] == 0:
                        reveal.append(neighbour)
                    elif self.backing_grid[neighbour[0]][neighbour[1]] == 1:
                        self.toggled[neighbour[0]][neighbour[1]] = True
                    elif self.backing_grid[neighbour[0]][neighbour[1]] == 2:
                        self.toggled[neighbour[0]][neighbour[1]] = True
                reveal.remove(cell)

    # mutator function for right click  
    def toggle_btn(self, i, j):
        if self.toggled[i][j]:
            return
        if self.flagged[i][j]:
            self.flagged[i][j] = False
            return 
        if self.backing_grid[i][j] == 0: 
            self.cascade_reveal(i, j)
        if self.backing_grid[i][j] == 'B':
            self.game_over = True
        print(self.game_over)
        
    # mutator function for right click
    def flag_btn(self, i, j):
        if self.flagged[i][j]:
            return
        if self.toggled[i][j]:
            self.flagged[i][j] = False
    
    # used for view to access
    def get_game_over(self):
        return self.game_over

    #gets the dictionary of neighbours
    def get_neighbours(self):
        return self.neighbours

    # gets the backing grid list of lists
    def get_grid(self):
        return self.backing_grid

    # gets the toggled boolean list of lists
    def get_toggled(self):
        return self.toggled

    # gets the toggled boolean list of lists
    def get_flagged(self):
        return self.flagged
    
