#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.messagebox as tkmsg
import sys
import time
import GameModel as gm

def left_handler(grid, board, i, j, mine):
    """ Called when left click on the (i, j) cell """
    if board[i][j]["image"] == "" and not grid.tab[i][j].revealed:
        board[i][j]["state"] = "disabled"
        board[i][j]["relief"] = tk.SUNKEN
        if grid.tab[i][j].is_bomb:
            board[i][j]["image"] = mine
            board[i][j]["state"] = "normal"
            end_game(False, grid, board)
        else:
            grid.tab[i][j].revealed = True
            gm.SQUARES_REVEALED += 1
            if grid.tab[i][j].bombs_around != 0:
                board[i][j]["text"] = grid.tab[i][j].bombs_around
            else:
                for (x, y) in gm.neighbours(i, j):
                    left_handler(grid, board, x, y, mine)
            if gm.SQUARES_REVEALED == (gm.WIDTH * gm.HEIGHT - gm.BOMBS):
                end_game(True, grid, board)


def right_handler(grid, board, i, j, flag):
    """ Called when right click on the (i, j) cell """
    if not grid.tab[i][j].revealed:
        if board[i][j]["image"] == "":
            board[i][j]["image"] = flag
            board[i][j]["state"] = "normal"
            gm.BOMBS_LEFT -= 1
        else:
            board[i][j]["state"] = "disabled"
            board[i][j]["image"] = ""
            gm.BOMBS_LEFT += 1


def end_game(win, grid, board):
    if win:
        title = "You won !"
        msg = "Good job. Play again ?"
    else:
        title = "You lost..."
        msg = "Try again ?"
    ans = tkmsg.askyesno(title, msg)
    if ans:
        start_new_game(grid, board)
    else:
        sys.exit()


def start_new_game(grid, board):
    for x in range(gm.HEIGHT):
        for y in range(gm.WIDTH):
            grid.tab[x][y].reset()
            board[x][y]["image"] = ""
            board[x][y]["text"] = ""
            board[x][y]["state"] = tk.DISABLED
            board[x][y]["relief"] = tk.RAISED
    grid.add_bombs()
    gm.SQUARES_REVEALED = 0
    gm.BOMBS_LEFT = gm.BOMBS
    gm.INIT_TIME = time.time()