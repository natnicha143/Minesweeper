from tkinter import * 
import tkinter.messagebox as tkmsg
import time

class Square:
    def __init__(self, master, controller, model):
        self.controller = controller
        self.model = model
        self.width = model.width
        self.height = model.height
        self.neighbours = model.neighbours
        self.backing_grid = model.backing_grid
        #creating images
        self.flag_img = PhotoImage(file="flag.png")
        self.mine_img = PhotoImage(file="mine.png")
        self.unclicked_img = PhotoImage(file="unclicked.png")
        self.clicked_img = PhotoImage(file="clicked.png")
        #create frame for tiles
        self.game_frame = Frame(master, borderwidth=2, relief=SUNKEN)
        #create tiles/buttons
        self.unclicked_button = Canvas(self, relief=FLAT)
        self.unclicked_button.pack()
        self.unclicked_button.create_image(0, 0, anchor=CENTER, image=self.unclicked_img)
        self.clicked_button = Canvas(self, relief=SUNKEN)
        self.clicked_button.pack()
        self.clicked_button.create_image(0, 0, anchor=CENTER, image=self.clicked_img)
        #create board of buttons
        self.buttons = self.get_buttons()
        self.game_frame.pack(padx=10, pady=10, side=BOTTOM)


    def game_over(self):
        for i in range(self.height):
            for j in range(self.width): 
                if self.backing_grid[i][j] == 'B':
                    self.buttons[i][j].itemconfig(image=self.mine_img, height=35, width=38, background='red', command='')
                else:
                    self.buttons[i][j].itemconfig(command='')
        tkmsg.showinfo("Mine sweeper", "Game Over!") 

    def activate_button(self, i, j):
        self.buttons[i][j].itemconfig(relief=SUNKEN, text=self.backing_grid[i][j], command='', background='pink')
        if self.backing_grid[i][j] == 'B':
            self.game_over()
        if self.backing_grid[i][j] == 0:
            self.cascade_reveal(i, j)

    def set_buttons(self):
        buttons = list()
        for row in range(self.height):
            buttons.append([])
            for col in range(self.width):
                buttons[row].append(Canvas(command=lambda i=row, j=col: activate_button(i, j)))
                buttons[row][col].grid(row=row, column=col)
        return buttons 

    def get_buttons(self):
        return self.buttons

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
        



    