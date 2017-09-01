from tkinter import *
from tkinter import messagebox
import time

import MineSweeperModel as ms
import GameView 

#Handles what happens when the left click occurs on the board
def cascade_reveal(i, j):
    reveal = list()
    adjacent = ms.neighbours[i, j]
    for neighbour in adjacent:
        if ms.backing_grid[neighbour[0]][neighbour[1]] == 0:
            reveal.append(neighbour)
    
    while reveal:
        for cell in reveal:
            adjacent = ms.neighbours[cell[0], cell[1]]
            if ms.backing_grid[cell[0]][cell[1]] == 0:
                GameView.buttons[cell[0]][cell[1]].configure(relief=SUNKEN, text='', background='pink', state='disabled')
                ms.backing_grid[cell[0]][cell[1]] = 's'
            for neighbour in adjacent:
                if ms.backing_grid[neighbour[0]][neighbour[1]] == 0:
                    reveal.append(neighbour)
                elif ms.backing_grid[neighbour[0]][neighbour[1]] == 1:
                    GameView.buttons[neighbour[0]][neighbour[1]].configure(relief=SUNKEN, text='1', background='pink', state='disabled')
                elif ms.backing_grid[neighbour[0]][neighbour[1]] == 2:
                    GameView.buttons[neighbour[0]][neighbour[1]].configure(relief=SUNKEN, text='2', background='pink', state='disabled')
            reveal.remove(cell)

def game_over():
    for i in range(ms.height):
        for j in range(ms.width): 
            if ms.backing_grid[i][j] == 'B':
                GameView.buttons[i][j].configure(image=GameView.mine, height=35, width=38, background='red', command='')
                title = "Game Over!"
                msg = "Play Again?"
                messagebox.askyesno(title, msg) 
            else:
                GameView.buttons[i][j].configure(command='')
                title = "You Won!"
                msg = "Play Again?"
            answer = messagebox.askyesno(title, msg)
            if answer:
                restart_game(grid, buttons)
            else:
                quit()


def left_click(i, j):
    GameView.buttons[i][j].configure(relief=SUNKEN, text=ms.backing_grid[i][j], command='', background='pink')
    if ms.backing_grid[i][j] == 'B':
        game_over()
    if ms.backing_grid[i][j] == 0:
        cascade_reveal(i, j)

def right_click(i, j):
    if not GameView.buttons[i][j].revealed:
        GameView.buttons[i][j].configure(image=GameView.flag, state="normal")
        ms.mines_left -= 1
    else:
        GameView.buttons[i][j].configure(command="")
        ms.mines_left += 1

def restart_game(grid, buttons):
    for row in range(ms.height):
        for col in range (ms.width):
            ms.backing_grid[i][j].reset()
            buttons[i][j].configure(state=DISABLED)
            buttons[i][j].configure(relief=RAISED)
    

    
###
