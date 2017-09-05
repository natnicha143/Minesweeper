from tkinter import *

#Extends tkinter's Frame class
class MainMenu(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.menu_frame = Frame(self.master, borderwidth=2, height=50, width=50)
    
        self.difficulty_img = PhotoImage(file="images/difficulty.png")
        self.mode_img = PhotoImage(file="images/gamemode.png")
        self.beginner_img = PhotoImage(file="images/beginner.png")
        self.intermediate_img = PhotoImage(file="images/intermediate.png")
        self.advanced_img = PhotoImage(file="images/advanced.png")
        self.sqsweeper_img = PhotoImage(file="images/squaresweeper.png")
        self.hexsweeper_img = PhotoImage(file="images/hexagonsweeper.png")
        self.coloursweeper_img = PhotoImage(file="images/coloursweeper.png")

        self.difficulty_btn = Button(self.menu_frame, image=self.difficulty_img, borderwidth=2)
        self.mode_btn = Button(self.menu_frame, image=self.mode_img, borderwidth=2)
        self.beginner_btn = Button(self.menu_frame, image=self.beginner_img, borderwidth=2)
        self.intermediate_btn = Button(self.menu_frame, image=self.intermediate_img, borderwidth=2)
        self.advanced_btn = Button(self.menu_frame, image=self.advanced_img, borderwidth=2)
        self.squaresweeper_btn = Button(self.menu_frame, image=self.sqsweeper_img, borderwidth=2)
        self.hexsweeper_btn = Button(self.menu_frame, image=self.hexsweeper_img, borderwidth=2)
        self.coloursweeper_btn = Button(self.menu_frame, image=self.coloursweeper_img, borderwidth=2)
