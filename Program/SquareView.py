from tkinter import * 
import tkinter.messagebox as tkmsg
import time

class Square:
    def __init__(self, master, controller, model, height, width):
        self.controller = controller
        self.model = model
        self.width = width
        self.height = height
        self.init_time = time.time()
        self.backing_grid = model.get_grid()
        self.neighbours = model.get_neighbours()
        #creating images
        self.flag_img = PhotoImage(file="images/flag.png")
        self.mine_img = PhotoImage(file="images/mine.png")
        #create frame for tiles
        self.game_frame = Frame(master, borderwidth=2, relief=SUNKEN, width=700, height=700)
        self.game_frame.pack(padx=10, pady=10, side=BOTTOM)                
        #top frame
        self.top_frame = Frame(master, borderwidth=2, height=40, relief=GROOVE, bg="#EA7CA1")
        self.top_frame.pack(padx=0, pady=0, side=TOP, fill="x")
        #create board of buttons
        self.current_col = 0
        self.current_row = 0
        self.buttons = self.create_buttons()
        self.timer()

    #creates buttons and stores within frame created, binds buttons to event_handler
    def create_buttons(self):
        buttons = list()
        for row in range(self.height):
            buttons.append([])
            for col in range(self.width):
                buttons[row].append(Button(self.game_frame, borderwidth=1, bg="#F597CA", height=2, width=5))
                buttons[row][col].grid(row=row, column=col)
                buttons[row][col].bind("<Button-1>", self.left_binding)
                buttons[row][col].bind("<Button-3>", self.right_binding)
                buttons[row][col].configure(command=lambda i=row, j=col: self.set_coordinates(i, j))
        return buttons 

    # sets the coordinates of each button
    def set_coordinates(self, i, j):
        self.current_row = i
        self.current_col = j

    # used for binding to button 1 (left click)
    def left_binding(self, event):
        self.controller.left_handler(self.current_row, self.current_col)
        self.display()
        if self.model.get_game_over() == True:
            self.display_mines()
    
    # used for displaying all mines on the board and if game_over is True

    def display_mines(self):
        for i in range(self.height):
            for j in range(self.width): 
                if self.backing_grid[i][j] == 'B':
                    self.buttons[i][j].configure(relief=SUNKEN, image=self.mine_img, command='', height=35, width=38)
        tkmsg.showinfo("Mine sweeper", "Game Over!") 
        self.game_frame.destroy()
        self.game_frame.quit()

    # used for binding to button 3 (right click)
    def right_binding(self, event):
        self.controller.right_handler(self.current_row, self.current_col)
        self.display()

    # display function for each situation apart from mine
    def display(self):
        backing_grid = self.model.get_grid()
        toggled = self.model.get_toggled()
        flagged = self.model.get_flagged()
        for i in range(self.width):
            for j in range(self.height):
                if toggled[i][j]:
                    if flagged[i][j]:
                        self.buttons[i][j].configure(image=self.flag_img, height=35, width=38)
                    else: 
                        self.buttons[i][j].configure(image="")
                else:
                    if backing_grid[i][j] == 0:
                        self.buttons[i][j].configure(relief=SUNKEN, text='', background='pink', state='disabled')
                    else:
                        self.buttons[i][j].configure(relief=SUNKEN, text=backing_grid[i][j], background='pink', state='disabled')


    # returns a list of buttons
    def get_buttons(self):
        return self.buttons

    # creates the timer in top frame
    def timer(self):
        timer_str = StringVar()
        timer_str.set(int((time.time() - self.init_time)//1))
        time_counter = Label(self.top_frame, height=1, width=4, bg='#EA7CA1', textvariable=timer_str)
        time_counter.grid(row=0, column=4, padx=5, sticky=E) 
  