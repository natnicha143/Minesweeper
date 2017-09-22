from tkinter import *

#Extends tkinter's Frame class
class MainMenu(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.menu_frame = Frame(master, borderwidth=2, bg="pink", height=2000, width=2000)
        self.menu_frame.pack()
        self.difficulty_img = PhotoImage(file="images/difficulty.png")
        self.beginner_img = PhotoImage(file="images/beginner.png")
        self.intermediate_img = PhotoImage(file="images/intermediate.png")
        self.advanced_img = PhotoImage(file="images/advanced.png")
        self.sqsweeper_img = PhotoImage(file="images/squaresweeper.png")

        self.squaresweeper_lbl = Label(self.menu_frame, image=self.sqsweeper_img)
        self.difficulty_lbl = Label(self.menu_frame, image=self.difficulty_img)
        self.difficulty_lbl.pack(fill=BOTH, expand=1)

        self.beginner_btn = Button(self.menu_frame, image=self.beginner_img, borderwidth=2, width=300, height=100)
        self.beginner_btn.pack()
        # self.beginner_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.intermediate_btn = Button(self.menu_frame, image=self.intermediate_img, borderwidth=2, width=300, height=100)
        self.intermediate_btn.pack()
        
        self.advanced_btn = Button(self.menu_frame, image=self.advanced_img, borderwidth=2, width=300, height=100)
        self.advanced_btn.pack()

        self.beginner_btn.configure(command=lambda: self.set_difficulty('beginner'))
        self.intermediate_btn.configure(command=lambda: self.set_difficulty('intermediate'))
        self.advanced_btn.configure(command=lambda: self.set_difficulty('advanced'))

    
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

    def get_settings(self):
        return [self.height, self.width, self.mines]
