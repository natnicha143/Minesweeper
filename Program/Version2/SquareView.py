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
        self.buttons = self.create_buttons()



    #creates buttons and stores within frame created, binds buttons to event_handler
    def create_buttons(self):
        buttons = list()
        for row in range(self.height):
            buttons.append([])
            for col in range(self.width):
                buttons[row].append(Button(self.game_frame, borderwidth=1, bg="#F597CA", height=1, width=3))
                buttons[row][col].grid(row=row, column=col)
                buttons[row][col].bind("<Button-1>", lambda: : self.button_bindings())
                buttons[row][col].bind("<Button-3>", lambda: : self.button_bindings())
        return buttons 

    def button_bindings(self, event, row, col):
        if event.type == 1:
            self.controller.left_handler(row, col)
        elif event.type == 3:
            self.controller.right_handler(row, col)
        else:
            raise Exception('Invalid event.')

    def game_over(self): 
        for i in range(self.height):
            for j in range(self.width): 
                if self.backing_grid == 'B':
                    self.buttons[i][j].configure(image="self.mine_img")
                    tkmsg.showinfo("Mine sweeper", "Game Over!") 
                    self.game_frame.destroy()
                    self.game_frame.quit()


    def display(self):
        backing_grid = self.model.get_grid()
        toggled = self.model.get_toggled()
        flagged = self.model.get_flagged()
        for i in range(self.width):
            for j in range(self.height):
                if toggled[i][j]:
                    if flagged[i][j]:
                        self.buttons[i][j].configure(image="self.flag_img")
                    else: 
                        self.buttons[i][j].configure(image="")
                else:
                    if backing_grid[i][j] == 0:
                        self.buttons[i][j].configure(relief=SUNKEN, text='', background='pink', state='disabled')
                    else:
                        self.buttons[i][j].configure(relief=SUNKEN, text=backing_grid[i][j], background='pink', state='disabled')



    def get_buttons(self):
        return self.buttons

    def timer(self):
        timer_str = StringVar()
        timer_str.set(int((time.time() - self.init_time)//1))
        time_counter = Label(self.top_frame, height=1, width=4, bg='#EA7CA1', textvariable=timer_str)
        time_counter.grid(row=0, column=4, padx=5, sticky=E)    
    # method in the view which looks at the backing_grid, toggles 
    # and covers from the model with 3 getters (in model) and configures all buttons to look like what the model is
    # Loops through every button and configures it based on how the model looks
    # There should be no checking of values in view...