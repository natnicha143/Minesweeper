from tkinter import * 
import tkinter.messagebox as tkmsg
import sys
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
                data = {"row": row, "col": col}
                buttons[row][col].bind("<Button-1>", lambda event, arg=data: self.left_binding(event, arg))
                buttons[row][col].bind("<Button-3>", lambda event, arg=data:  self.right_binding(event, arg))
        return buttons 

    # used for binding to button 1 (left click)
    def left_binding(self, event, arg):
        if self.model.get_game_over() or self.model.get_game_win():
            return
        self.controller.left_handler(arg["row"], arg["col"])
        self.display()
        if self.model.get_game_over():
            self.game_end()

    # used for binding to button 3 (right click)
    def right_binding(self, event, arg):
        if self.model.get_game_over() or self.model.get_game_win():
            return
        self.controller.right_handler(arg["row"], arg["col"])
        print(self.model.get_game_win())
        self.display()
        if self.model.get_game_win():
            title = "You won!"
            msg = "Good job. Play again?"
            ans = tkmsg.askyesno(title, msg)
            if ans:
                self.return_main()
            else:
                sys.exit()

                
        
    # used for displaying all mines on the board and if game_over is True

    def game_end(self):
        for i in range(self.height):
            for j in range(self.width): 
                if self.backing_grid[i][j] == 'B':
                    self.buttons[i][j].configure(relief=SUNKEN, image=self.mine_img, height=35, width=38, bg='#EA7CA1')
        title = "You Lost..."
        msg = "Bad luck. Try again?"
        ans = tkmsg.askyesno(title, msg)
        if ans:
            self.return_main()
        else:
            sys.exit()


    # display function for each situation apart from mine
    def display(self):
        backing_grid = self.model.get_grid()
        toggled = self.model.get_toggled()
        flagged = self.model.get_flagged()
        for i in range(self.width):
            for j in range(self.height):
                if toggled[i][j]:
                    if backing_grid[i][j] == 0 or backing_grid[i][j] == 's':
                        self.buttons[i][j].configure(relief=SUNKEN, text='', background='pink', state='disabled')
                    else:
                        self.buttons[i][j].configure(relief=SUNKEN, text=backing_grid[i][j], background='pink', state='disabled')
                else:
                    if flagged[i][j]:
                        self.buttons[i][j].configure(image=self.flag_img, height=35, width=38, bg='#EA7CA1')
                    else: 
                        self.buttons[i][j].configure(image="", height=2, width=5)



    # returns a list of buttons
    def get_buttons(self):
        return self.buttons


    # creates the timer in top frame
    def timer(self):
        self.update_time_counter()
        time_counter = Label(self.top_frame, height=1, width=10, bg='#EA7CA1', textvariable=self.time_counter_str)
        time_counter.grid(row=0, column=1, sticky=W)

    def return_main(self):
        self.game_frame.destroy()
        self.top_frame.destroy()
        self.game_frame.quit()

    # creates new game button in top frame
    def new_game_button(self):
        newgame_button = Button(self.top_frame, bd=1, width=15, text="New game", bg="#995179")
        newgame_button.grid(row=0, column=10, padx=2, sticky=E)
        newgame_button.configure(command=lambda: self.return_main())
 
    def update_time_counter(self):
        if not self.model.get_game_over() and not self.model.get_game_win():
            self.time_counter_str.set(int((time.time() - self.init_time)//1))
            self.top_frame.after(100, self.update_time_counter)



