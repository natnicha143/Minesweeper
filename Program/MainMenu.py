from tkinter import *

#Extends tkinter's Frame class
class MainMenu(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        # create main menu frame
        self.menu_frame = Frame(master, borderwidth=2, bg="pink", width=650, height=600)
        self.menu_frame.pack()
        # create images for menu
        self.difficulty_img = PhotoImage(file="images/difficulty.png")
        self.beginner_img = PhotoImage(file="images/beginner.png")
        self.intermediate_img = PhotoImage(file="images/intermediate.png")
        self.advanced_img = PhotoImage(file="images/advanced.png")
        self.logo = PhotoImage(file="images/squaresweeper.png")
        # give each image a tkinter type
        self.logo_lbl = Label(self.menu_frame, image=self.logo, width=250, bg="pink")
        self.logo_lbl.place(height=110, width=350, x=150, y=25)
        
        self.difficulty_lbl = Label(self.menu_frame, image=self.difficulty_img, bg="pink")
        self.difficulty_lbl.place(height=90, width=350, x=150, y=150)

        self.beginner_btn = Button(self.menu_frame, image=self.beginner_img, borderwidth=2, bg="pink")
        self.beginner_btn.place(height=75, width=288, x=180, y=250)

        self.intermediate_btn = Button(self.menu_frame, image=self.intermediate_img, borderwidth=2, bg="pink")
        self.intermediate_btn.place(height=75, width=288, x=180, y=350)
        
        self.advanced_btn = Button(self.menu_frame, image=self.advanced_img, borderwidth=2, bg="pink")
        self.advanced_btn.place(height=75, width=288, x=180, y=450)

        # configure buttons to get the settings for each button
        self.beginner_btn.configure(command=lambda: self.set_difficulty('beginner'))
        self.intermediate_btn.configure(command=lambda: self.set_difficulty('intermediate'))
        self.advanced_btn.configure(command=lambda: self.set_difficulty('advanced'))

    # used to set the parameters of the game
    def set_difficulty(self, x):
        if x == 'beginner':
            self.mines = 10
            self.height = 9
            self.width = 9
        elif x == 'intermediate':
            self.mines = 40
            self.height = 16
            self.width = 16
        elif x == 'advanced':
            self.mines = 90
            self.height = 24
            self.width = 24
        self.menu_frame.destroy()
        self.menu_frame.quit()

    # gets the settings stored in set_difficulty
    def get_settings(self):
        return [self.height, self.width, self.mines]
