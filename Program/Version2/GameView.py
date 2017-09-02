from tkinter import * 
import tkinter.font as tkf
import time
import ButtonController 
controller = ButtonController.ButtonController()

def create_main_window():
    window = Tk()
    window.title("Mine Sweeper")
    window["bg"] = "white"
    window.resizable(width=False, height=False)
    return window

def create_images():
    flag = PhotoImage(file="flag.png")
    mine = PhotoImage(file="mine.png")
    return (flag, mine)

def create_board(window, GRID, flag, mine):
    ms_frame = Frame(window, borderwidth=2, relief=SUNKEN, bg="black")

    def create_tile(i, j):
        f = Frame(ms_frame, height=30, width=30)
        b = Button(f, borderwidth=1, state="normal", bg="pink")
        b.pack(fill=BOTH, expand=True)
        # buttons bindings
        def event_handler(event, x=i, y=j):
            if event.num == 1:
                controller.left_handler(GRID, BOARD, i, j, mine)
            elif event.num == 3:
                controller.right_handler(GRID, BOARD, i, j, flag)
            else:
                raise Exception('Invalid event code.')
        b.bind("<Button-1>", event_handler)
        b.bind("<Button-3>", event_handler)

        f.pack_propagate(False)
        f.grid(row=i, column=j)
        return b

    BOARD = [[create_tile(i, j) for j in range(gm.WIDTH)] for i in range(gm.HEIGHT)]
    ms_frame.pack(padx=10, pady=10, side=BOTTOM)
    return BOARD

#~.~.~.~.~ Creating Frames and displaying Restart button, Timer and Remaining number of mines within top frame

def create_top_frame(window, grid, board):
    top_frame = Frame(window, borderwidth=2, height=40, relief=GROOVE, bg="#EA7CA1")
    top_frame.pack(padx=0, pady=0, side=TOP, fill="x")
    for i in range(4):
        top_frame.columnconfigure(i, weight=1)
    mine_counter(top_frame)
    create_new_game_button(top_frame, grid, board)
    create_time_counter(top_frame)
    return top_frame


def mine_counter(top_frame):
    """ mines_counter, left """
    mine_counter_str = StringVar()

    def update_mines():
        mine_counter_str.set(gm.REMAINING_MINES)
        top_frame.after(100, update_mines)
    update_mines()

    mines_counter = Label(   top_frame, height=1, width=4, bg="#EA7CA1", 
                                textvariable=mine_counter_str, 
                                font=tkf.Font(weight='bold', size=10))
    mines_counter.grid(row=0, column=0, padx=5, sticky=W)


def create_new_game_button(top_frame, grid, board):
    """ new game button, middle left """
    def _start_new_game(g=grid, b=board):
        controller.start_new_game(grid, board)

    newgame_button = Button( top_frame, bd=1, width=15, text="New game",
                                command=_start_new_game, bg="#EA7CA1")
    newgame_button.grid(row=0, column=1, padx=0, sticky=E)



def create_time_counter(top_frame):
    """ time counter, right """
    time_counter_str = StringVar()

    def update_time_counter():
        time_counter_str.set(int((time.time() - gm.INIT_TIME)//1))
        top_frame.after(100, update_time_counter);
    update_time_counter();

    time_counter = Label(top_frame, height=1, width=4, bg='#EA7CA1',
                            textvariable=time_counter_str,
                            font=tkf.Font(slant='italic', size=10))
    time_counter.grid(row=0, column=4, padx=5, sticky=E)
