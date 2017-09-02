#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.messagebox as tkmsg
import sys
import time
import MineSweeperModel as model


class ButtonController():
    def __init__(self, model):
        self.model = model

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
                model.TILES_REVEALED += 1
                if grid.buttons[i][j].neighbour_mines != 0:
                    board[i][j]["text"] = grid.buttons[i][j].neighbour_mines
                else:
                    for (x, y) in model.neighbours[i, j]:
                        self.left_handler(grid, board, x, y, mine)
                if model.TILES_REVEALED == (model.WIDTH * model.HEIGHT - model.MINES):
                    self.end_game(True, grid, board)


    def right_handler(self, grid, board, i, j, flag):
        """ Called when right click on the (i, j) cell """
        if not grid.buttons[i][j].revealed:
            if board[i][j]["image"] == "":
                board[i][j]["image"] = flag
                board[i][j]["state"] = "normal"
                model.REMAINING_MINES -= 1
            else:
                board[i][j]["state"] = "disabled"
                board[i][j]["image"] = ""
                model.REMAINING_MINES += 1


    def end_game(self, win, grid, board):
        if win:
            title = "You won !"
            msg = "Good job. Play again ?"
        else:
            title = "You lost..."
            msg = "Try again ?"
        ans = tkmsg.askyesno(title, msg)
        if ans:
            self.start_new_game(grid, board)
        else:
            sys.exit()


    def start_new_game(self, grid, board):
        for x in range(model.HEIGHT):
            for y in range(model.WIDTH):
                grid.buttons[x][y].reset()
                board[x][y]["image"] = ""
                board[x][y]["text"] = ""
                board[x][y]["state"] = tk.DISABLED
                board[x][y]["relief"] = tk.RAISED
        grid.generate_mines()
        model.TILES_REVEALED = 0
        model.REMAINING_MINES = model.MINES
        model.INIT_TIME = time.time()