import tkinter as tk
import sys
import time

class BoardController:
    def __init__(self, model, board):
        self.model = model
        self.board = board
        self.neighbours = self.model.get_neighbours()


    def left_handler(self, grid, board, i, j, mine):
        """ Called when left click on the (i, j) cell """
        if board[i][j]["image"] == "" and not grid.buttons[i][j].revealed:
            board[i][j]["state"] = "disabled"
            board[i][j]["relief"] = tk.SUNKEN
            if grid.buttons[i][j].is_mine:
                board[i][j]["image"] = mine
                board[i][j]["state"] = "normal"
                self.end_game(False, grid, board)
            else:
                grid.buttons[i][j].revealed = True
                self.model.TILES_REVEALED += 1
                if grid.buttons[i][j].neighbour_mines != 0:
                    board[i][j]["text"] = grid.buttons[i][j].neighbour_mines
                else:
                    for (x, y) in self.neighbours[i, j]:
                        self.left_handler(grid, board, x, y, mine)
                if self.model.tiles_revealed == (self.model.width * self.model.height - self.model.mines):
                    self.end_game(True, grid, board)


    def right_handler(self, grid, board, i, j, flag):
        """ Called when right click on the (i, j) cell """
        if not grid.buttons[i][j].revealed:
            if board[i][j]["image"] == "":
                board[i][j]["image"] = flag
                board[i][j]["state"] = "normal"
                self.model.mines_remain -= 1
            else:
                board[i][j]["state"] = "disabled"
                board[i][j]["image"] = ""
                self.model.mines_remain += 1


    def start_new_game(self, self.grid, self.board):
        for x in range(self.model.height):
            for y in range(self.model.width):
                grid.buttons[x][y].reset()
                board[x][y]["image"] = ""
                board[x][y]["text"] = ""
                board[x][y]["state"] = tk.DISABLED
                board[x][y]["relief"] = tk.RAISED
        self.grid.generate_mines()
        self.model.tiles_revealed = 0
        self.model.mines_remain = self.model.mines
        self.model.init_time = time.time()