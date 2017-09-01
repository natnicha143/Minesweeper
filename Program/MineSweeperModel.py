
import random as rand
import time
import MineSweeperGame as game
import MineSweeperModel as ms
#~.~.~.~.~.~.~.~.~.~.~.~
height = 10
width = 15
size = height * width
mines = 20
mines_left = mines
tiles_revealed = 0
init_time = time.time()
#~.~.~.~.~.~.~.~.~.~.~.~

def init_game():
    print("Beginner/Intermediate/Advanced?: ")
    diff = int(input())
    if diff == 1:
        m = 10
        width = 9
        height = 9
    elif diff == 2:
        mines = 40
        width = 16
        height = 16
    elif diff == 3:
        mines = 90
        width = 24
        height = 24


def find_neighbours():
    neighbours = dict()
    for row in range(height):
        for col in range(width):
            adjacent = list()
            #D O W N 
            if row+1 < height:
                adjacent.append([row+1, col]) 
            #D O W N  L E F T
            if 0 <= row+1 < height and 0 <= col-1:
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
            if row+1 < height and col+1 < width:
                adjacent.append([row+1, col+1])
            neighbours[row, col] = adjacent
    return neighbours  


def mine_exists(row, col):
    for mine in mine_pos:
        if mine[0] == row and mine[1] == col:
            return True
    return False 


def generate_mines():
        mines = list()
        for i in range(ms.size * ms.mines):
            #generate coordinates for mines
            x = rand.randrange(0, ms.size)
            y = rand.randrange(0, ms.size)
            mines.append([x, y])
        return mines 


def apply_numeric(neighbours, mine_pos):
    backing_grid = [[0 for col in range(width)] for row in range(height)]
    for row in range(height):
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


################
neighbours = find_neighbours()
mine_pos = generate_mines()
backing_grid = apply_numeric(neighbours, mine_pos)
