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
        self.top_frame = Frame(master, borderwidth=2, relief=GROOVE, bg="#EA7CA1")
        self.top_frame.pack(padx=0, pady=0, side=TOP, fill="x")
        #create board of buttons
        self.current_col = 0
        self.current_row = 0
        self.buttons = self.create_buttons()
        self.time_counter_str = StringVar()
        self.set_timer = self.timer()
        self.new_game = self.new_game_button()


    #creates buttons and stores within frame created, binds buttons to event_handler
    def create_buttons(self):
        buttons = list()
        for row in range(self.height):
            buttons.append([])
            for col in range(self.width):
                buttons[row].append(Button(self.game_frame, borderwidth=1, bg='#EA7CA1', height=2, width=5))
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
            self.game_end()
    
    # used for displaying all mines on the board and if game_over is True

    def game_end(self):
        for i in range(self.height):
            for j in range(self.width): 
                if self.backing_grid[i][j] == 'B':
                    self.buttons[i][j].configure(relief=SUNKEN, image=self.mine_img, command='', height=35, width=38, bg='#EA7CA1')
        tkmsg.showinfo("Mine sweeper", "Game Over!") 

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
                    if backing_grid[i][j] == 0 or 's':
                        self.buttons[i][j].configure(relief=SUNKEN, text='', background='pink', state='disabled')
                    else:
                        self.buttons[i][j].configure(relief=SUNKEN, text=backing_grid[i][j], background='pink', state='disabled')
                else:
                    if flagged[i][j]:
                        self.buttons[i][j].configure(image=self.flag_img, height=35, width=38, bg='#EA7CA1')
                    else: 
                        self.buttons[i][j].configure(image="")



    # returns a list of buttons
    def get_buttons(self):
        return self.buttons


    # creates the timer in top frame
    def timer(self):
        self.update_time_counter()
        time_counter = Label(self.top_frame, height=1, width=4, bg='#EA7CA1', textvariable=self.time_counter_str)
        time_counter.grid(row=0, column=1, sticky=W)

    # creates new game button in top frame
    def new_game_button(self):
        newgame_button = Button(self.top_frame, bd=1, width=15, text="New game", command='', bg="#EA7CA1")
        newgame_button.grid(row=0, column=2, padx=2, sticky=E)

    def update_time_counter(self):
        self.time_counter_str.set(int((time.time() - self.init_time)//1))
        self.top_frame.after(100, self.update_time_counter)


