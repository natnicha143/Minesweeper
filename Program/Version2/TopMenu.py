from tkinter import * 
import time 

class TopMenu:
    def __init__(self, master, model, view, board):
        self.master = master
        self.model = model
        self.view = view 
        self.board = board
        self.backing_grid = backing_grid
        self.top_frame = Frame(self.master, borderwidth=2, height=40, relief=GROOVE, bg="#EA7CA1")
        self.top_frame.pack(padx=0, pady=0, side=TOP, fill="x")
        for i in range(4):
            self.top_frame.columnconfigure(i, weight=1)
        self.mine_counter(self.top_frame)
        self.create_new_game_button(self.top_frame, self.backing_grid, self.board)
        self.create_time_counter(self.top_frame)


    def mine_counter(self, self.top_frame):
        mine_counter_str = StringVar()
        def update_mines(self):
            mine_counter_str.set(self.model.mines_remain)
            top_frame.after(100, self.update_mines)
        self.update_mines()
        mines_counter = Label(top_frame, height=1, width=4, bg="#EA7CA1", textvariable=mine_counter_str)
        mines_counter.grid(row=0, column=0, padx=5, sticky=W)


    def create_new_game_button(self, self.top_frame, self.backing_grid, self.board):
        def _start_new_game(self, g=self.backing_grid, b=self.board):
            self.controller.start_new_game(self.backing_grid, self.board)

        newgame_button = Button(top_frame, bd=1, width=15, text="New game", command=_start_new_game, bg="#EA7CA1")
        newgame_button.grid(row=0, column=1, padx=0, sticky=E)


    def create_time_counter(self, top_frame):
        time_counter_str = StringVar()
        def update_time_counter(self):
            time_counter_str.set(int((time.time() - self.model.INIT_TIME)//1))
            top_frame.after(100, update_time_counter)
        update_time_counter()

        time_counter = Label(top_frame, height=1, width=4, bg='#EA7CA1', textvariable=time_counter_str)
        time_counter.grid(row=0, column=4, padx=5, sticky=E)
