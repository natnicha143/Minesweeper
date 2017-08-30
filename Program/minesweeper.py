#NATNICHA TITIPHANPONG
import random as rand
import time
from tkinter import *
from tkinter import messagebox


def populate_game():
    neighbours = dict()
    for row in range(length):
        for col in range(width):
            adjacent = list()
            #D O W N 
            if row+1 < length:
                adjacent.append([row+1, col]) 
            #D O W N  L E F T
            if 0 <= row+1 < length and 0 <= col-1:
                adjacent.append([row+1, col-1])
            #L E F T
            if col-1 >= 0:
                adjacent.append([row, col-1])
            #T O P  L E F T
            if 0 <= row-1 and 0 <= col-1:
                adjacent.append([row-1, col-1])
            #T O P
            if row-1 >= 0:
                adjacent.append([row-1, col])
            #T O P  R I G H T
            if 0 <= row-1 and col+1 < width:
                adjacent.append([row-1, col+1])
            #R I G H T
            if col+1 < width:
                adjacent.append([row, col+1])
            #D O W N  R I G H T
            if row+1 < length and col+1 < width:
                adjacent.append([row+1, col+1])
            neighbours[row, col] = adjacent
    return neighbours  


def generate_mines():
    mines = list()
    for i in range(size * mine_percentage):
       #generate coordinates for mines
       x = rand.randrange(0, size)
       y = rand.randrange(0, size)
       mines.append([x, y])
    return mines 


def mine_exists(row, col):
    for mine in mines:
        if mine[0] == row and mine[1] == col:
            return True
    return False 


def apply_numeric(neighbours, mines):
    backing_grid = [[0 for col in range(width)] for row in range(length)]
    for row in range(length):
        for col in range (width):
            count = 0
            if mine_exists(row, col):
                backing_grid[row][col] = 'B'
            else:
                for neighbour in neighbours[row, col]:
                    if mine_exists(neighbour[0], neighbour[1]):
                        count += 1
                backing_grid[row][col] = count
    return backing_grid


#look through each adjacent square and if it has no number or mine, add it's adjacent squares 
def cascade_reveal(i, j):
    reveal = []
    adjacent = neighbours[i, j]
    for neighbour in adjacent:
        if backing_grid[neighbour[0]][neighbour[1]] == 0:
            reveal.append(neighbour)
    
    while reveal:
        for cell in reveal:
            adjacent = neighbours[cell[0], cell[1]]
            if backing_grid[cell[0]][cell[1]] == 0:
                buttons[cell[0]][cell[1]].configure(relief=SUNKEN, text='', background='pink', state='disabled')
                backing_grid[cell[0]][cell[1]] = 's'
            for neighbour in adjacent:
                if backing_grid[neighbour[0]][neighbour[1]] == 0:
                    reveal.append(neighbour)
                elif backing_grid[neighbour[0]][neighbour[1]] == 1:
                    buttons[neighbour[0]][neighbour[1]].configure(relief=SUNKEN, text='1', background='pink', state='disabled')
                elif backing_grid[neighbour[0]][neighbour[1]] == 2:
                    buttons[neighbour[0]][neighbour[1]].configure(relief=SUNKEN, text='2', background='pink', state='disabled')
            reveal.remove(cell)


def game_over():
    for i in range(length):
        for j in range(width): 
            if backing_grid[i][j] == 'B':
                buttons[i][j].configure(image=img, height=35, width=38, background='red', command='')
            else:
                buttons[i][j].configure(command='')
    messagebox.showinfo("Mine sweeper", "Game Over!")

# def game_won():
    

def activate_button(i, j):
    buttons[i][j].configure(relief=SUNKEN, text=backing_grid[i][j], command='', background='pink')
    if backing_grid[i][j] == 'B':
        game_over()
    if backing_grid[i][j] == 0:
        cascade_reveal(i, j)


def set_buttons():
    buttons = list()
    for row in range(length):
        buttons.append([])
        for col in range(width):
            buttons[row].append(Button(bg="#F597CA", height=2, width=5, command=lambda i=row, j=col: activate_button(i, j)))
            buttons[row][col].grid(row=row, column=col)
    return buttons 


def reset_program():
    neighbours = populate_game()
    buttons = set_buttons()
    mines = generate_mines()
    backing_grid = apply_numeric(neighbours, mines) 

#~.~.~.~ Main ~.~.~.~#

print("Beginner/Intermediate/Advanced?: ")
diff = int(input())
if diff == 1:
    mine_percentage = 10
    width = 9
    length = 9
elif diff == 2:
    mine_percentage = 40
    width = 16
    length = 16
elif diff == 3:
    mine_percentage = 80
    width = 24
    length = 24

size = width * length
neighbours = populate_game()
mines = generate_mines()
backing_grid = apply_numeric(neighbours, mines)
buttons = set_buttons(
img = PhotoImage(file="mine.png")
#~.~.~.~.~.~.~.~


#~.~.~.~.~.~.~.~
root = Tk()
root.withdraw()
root.title("Mine sweeper")
frame = Frame(root, height=400, width=400, bg='black')
frame.pack(side=LEFT, expand=1)




# quitButton = Button(text="Quit", command=quit)
# resetButton = Button(root, text="Restart", command=reset_program).pack()
#initialises choice
#levels = [("Beginner", 1), ("Intermediate", 2), ("Advanced", 3)]

#Label(root, text="""Select a difficulty:""", justify = RIGHT, padx = 20).pack()

root.mainloop()
