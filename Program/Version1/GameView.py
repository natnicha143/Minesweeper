from tkinter import *
from tkinter import messagebox
import time

import ButtonController as bc
import MineSweeperModel as ms
import MineSweeperGame as game

def main_window():
    master = Tk()
    master.title("Mine Sweeper")
    master["bg"] = "white"
    master.resizable(width=False, height=False)
    return master

def create_image():
    mine = PhotoImage(file="mine.png")
    flag = PhotoImage(file="flag.png")
    return(mine, flag)

def create_board(master, grid, mine, flag):
    frame = Frame(master, borderwidth=2, relief=SUNKEN)

    def create_button(i, j):
        f = Frame(frame, height=30, width=30)
        b = Button(f, borderwidth=1, bg="#F597CA")
        b.pack(fill=BOTH, expand=True)
      
        def button_bindings(event, i, j):
            if event.type == 1:
                bc.left_click(grid, board, i, j)
            elif event.type == 3:
                bc.right_click(grid, board, i, j)
            else:
                raise Exception('Invalid event.')
        b.bind("<Button-1>", button_bindings)
        b.bind("<Butotn-3>", button_bindings)

        f.pack_propagate(False)
        f.grid(row=i, column=j)
        return b

    board = [[create_button(i, j) for col in range(ms.width)] for row in range(ms.height)]
    frame.pack(padx=10, pady=10, side=BOTTOM)
    return board


def make_top_frame(window, grid, buttons):
    top_frame = Frame(window, borderwidth=2, height=35, relief=GROOVE)
    top_frame.pack(padx=0, pady=0, sider=TOP, fill="x")
    for i in range(4):
        top_frame.columnconfigure(i, weight=1)
    mine_counter(top_frame)
    new_game_btn(top_frame, grid, buttons)
    time_counter(top_frame)
    return top_frame

def mine_counter(top_frame):
    mine_counter_str = StringVar()
    def update_counter():
        mine_counter_str.set(ms.mines_left)
        top_frame.after(100, update_counter)
    update_counter()

    mine_counter = Label(top_frame, height=1, width=4, bg="pink", textvariable=mine_counter_str)
    mine_counter.grid(row=0, column=0, padx=5, sticky=W)


def new_game_btn(top_frame, grid, buttons):
    def start_new():
        bc.restart_game(grid, buttons)

    new_game_btn = Button(top_frame, bd=1, width=15, text="New game", command=start_new)
    new_game_btn.grid(row=0, column=3, padx=0, sticky=W)

def time_counter(top_frame):
    time_counter_str = StringVar()

    def update_counter():
        time_counter_str.set(int((time.time() - ms.init_time)//1))
        top_frame.after(100, update_counter)
    update_counter()

    time_counter = Label(top_frame, height=1, width=4, bg='pink', textvariable=time_counter_str)
    time_counter.grid(row=0, column=4, padx=5, sticky=E)

master = main_window()
grid = game.Grid()
mine, flag = create_image()
board = create_board(master, grid, mine, flag)