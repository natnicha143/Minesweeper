from tkinter import * 
import tkinter.messagebox as tkmsg
import time

class Util:
    def __init__(self):
        self.start_new_game = 

    def end_game(self, win):
        if win:
        title = "You won! Hooray!"
        msg = "Good job! Play again?"
    else:
        title = "You lost..."
        msg = "Play again?"
    ans = tkmsg.askyesno(title, msg)
    if ans:
        self.start_new_game(self.backing_grid, self.board)
    else:
        sys.exit()