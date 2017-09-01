import GameView
import MineSweeperModel as ms 

###Main
#Set paramters
ms.init_game()

grid = Grid()
grid.generate_mines()

## GUI
master = GameView.main_window()
mine, flag = GameView.create_image()
board = GameView.create_board(master, grid, mine, flag)
top_frame = GameView.make_top_frame(master, grid, board)

mainloop()