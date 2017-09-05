from tkinter import * 
import tkinter.messagebox as tkmsg
import time

class Square:
    def __init__(self, master, controller, model, width, height, backing_grid):
        self.controller = controller
        self.model = model
        self.width = width
        self.height = height
        self.backing_grid = backing_grid
        #creating images
        self.flag_img = PhotoImage(file="flag.png")
        self.mine_img = PhotoImage(file="mine.png")
        #create frame for tiles
        self.ms_frame = Frame(master, borderwidth=2, relief=SUNKEN)
        #create tiles/buttons
        #create board of buttons
        self.board = [[self.create_buttons(i, j) for col in range(self.width)] for row in range(self.height)]
        self.ms_frame.pack(padx=10, pady=10, side=BOTTOM)

    # buttons bindings for events, called by create_buttons
    def event_handler(self, event, x=i, y=j):
        if event.num == 1:
            self.controller.left_handler(self.board, i, j, self.flag_img)
        elif event.num == 3:
            self.controller.right_handler(self.board, i, j, self.mine_img)

    #creates buttons and stores within frame created, binds buttons to event_handler
    def create_buttons(self, i, j):
        f = Frame(self.ms_frame, height=30, width=30)
        b = Button(f, borderwidth=1, state="normal", bg="pink")
        b.pack(fill=BOTH, expand=True)
        f.pack_propagate(False)
        f.grid(row=i, column=j)
        b.bind("<Button-1>", self.event_handler)
        b.bind("<Button-3>", self.event_handler)
        return b

    # def set_parameters(self, argv):
        



    