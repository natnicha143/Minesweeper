#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports ######################################################################
import tkinter as tk
import tkinter.font as tkf
import time
import GameModel as gm
import ButtonController


# Main unresizable window ######################################################
def create_main_window():
    window = tk.Tk()
    window.title("Mine Sweeper")
    window["bg"] = "white"
    window.resizable(width=False, height=False)
    return window


# Images #######################################################################
def create_images():
    flag = tk.PhotoImage(file="flag.png")
    mine = tk.PhotoImage(file="mine.png")
    return (flag, mine)


# Game frame ###################################################################
def create_board(window, GRID, flag, mine):
    game_frame = tk.Frame(window, borderwidth=2, relief=tk.SUNKEN)

    def create_square(i, j):
        f = tk.Frame(game_frame, height=30, width=30)
        s = tk.Button(f, borderwidth=1, state="normal",
                        disabledforeground="#000000", bg="pink")
        s.pack(fill=tk.BOTH, expand=True)

        # buttons bindings
        def __handler(event, x=i, y=j):
            if event.num == 1:
                ButtonController.left_handler(GRID, BOARD, i, j, mine)
            elif event.num == 3:
                ButtonController.right_handler(GRID, BOARD, i, j, flag)
            else:
                raise Exception('Invalid event code.')
        s.bind("<Button-1>", __handler)
        s.bind("<Button-3>", __handler)

        f.pack_propagate(False)
        f.grid(row=i, column=j)
        return s

    BOARD = [[create_square(i, j)   for j in range(gm.WIDTH)] 
                                    for i in range(gm.HEIGHT)]
    game_frame.pack(padx=10, pady=10, side=tk.BOTTOM)
    return BOARD


# Top frame ####################################################################

def create_top_frame(window, grid, board):
    top_frame = tk.Frame(window, borderwidth=2, height=40, relief=tk.GROOVE)
    top_frame.pack(padx=0, pady=0, side=tk.TOP, fill="x")
    for i in range(4):
        top_frame.columnconfigure(i, weight=1)
    create_bombs_counter(top_frame)
    create_new_game_button(top_frame, grid, board)
    create_time_counter(top_frame)
    return top_frame


def create_bombs_counter(top_frame):
    """ bombs_counter, left """
    bombs_counter_str = tk.StringVar()

    def update_bombs_counter():
        bombs_counter_str.set(gm.BOMBS_LEFT)
        top_frame.after(100, update_bombs_counter)
    update_bombs_counter()

    bombs_counter = tk.Label(   top_frame, height=1, width=4, bg='pink', 
                                textvariable=bombs_counter_str, 
                                font=tkf.Font(weight='bold', size=10))
    bombs_counter.grid(row=0, column=0, padx=5, sticky=tk.W)


def create_new_game_button(top_frame, grid, board):
    """ new game button, middle left """
    def _start_new_game(g=grid, b=board):
        ButtonController.start_new_game(grid, board)

    newgame_button = tk.Button( top_frame, bd=1, width=15, text="New game",
                                command=_start_new_game, bg="#EA7CA1")
    newgame_button.grid(row=0, column=1, padx=0, sticky=tk.E)



def create_time_counter(top_frame):
    """ time counter, right """
    time_counter_str = tk.StringVar()

    def update_time_counter():
        time_counter_str.set(int((time.time() - gm.INIT_TIME)//1))
        top_frame.after(100, update_time_counter);
    update_time_counter();

    time_counter = tk.Label(top_frame, height=1, width=4, bg='#EA7CA1',
                            textvariable=time_counter_str,
                            font=tkf.Font(slant='italic', size=10))
    time_counter.grid(row=0, column=4, padx=5, sticky=tk.E)
