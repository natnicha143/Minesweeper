from tkinter import * 
import time
import ButtonController as controller
import MineSweeperModel as model

class GameView():
    def __init__(self, controller, model):
        self.controller = controller
        self.model = model

    def create_main_window(self):
        window = Tk()
        window.title("Mine Sweeper")
        window["bg"] = "black"
        window.resizable(width=False, height=False)
        return window

    def create_images(self):
        flag = PhotoImage(file="flag.png")
        mine = PhotoImage(file="mine.png")
        return (flag, mine)

        # buttons bindings
    def event_handler(self, event, x=i, y=j, BOARD, GRID, flag, mine):
        if event.num == 1:
            self.controller.left_handler(GRID, BOARD, i, j, mine)
        elif event.num == 3:
            self.controller.right_handler(GRID, BOARD, i, j, flag)

    def create_board(self, window):
        ms_frame = Frame(window, borderwidth=2, relief=SUNKEN, bg="black")

    def create_tile(self, i, j, ms_frame):
        f = Frame(ms_frame, height=30, width=30)
        b = Button(f, borderwidth=1, state="normal", bg="pink")
        b.pack(fill=BOTH, expand=True)
        f.pack_propagate(False)
        f.grid(row=i, column=j)
        b.bind("<Button-1>", self.event_handler)
        b.bind("<Button-3>", self.event_handler)
        return b


    def set_parameters(self, argv):
            # if there's not 3 args
        if len(argv) != 3:
            if len(argv) != 0:
                print("Warning : Invalid parameters")
                print("Need 3 arguments (height, WIDTH, mines)")
            return

        # if they aren't ints
        try:
            height = int(argv[0])
            WIDTH = int(argv[1])
            mines = int(argv[2])
        except ValueError:
            print("Warning : Invalid parameters")
            print("Arguments aren't ints")
            return

        # if constraints aren't respected
        if  height <= 0 or WIDTH <= 0 or mines <= 0 or mines >= height*WIDTH:
            print("Warning : Invalid parameters")
            print("Can't create game with these values")
            return

        HEIGHT = height
        WIDTH = WIDTH
        MINES = mines
        REMAINING_MINES = mines
    #~.~.~.~.~ Creating Frames and displaying Restart button, Timer and Remaining number of mines within top frame

    def create_top_frame(self, window, grid, board):
        top_frame = Frame(window, borderwidth=2, height=40, relief=GROOVE, bg="#EA7CA1")
        top_frame.pack(padx=0, pady=0, side=TOP, fill="x")
        for i in range(4):
            top_frame.columnconfigure(i, weight=1)
        self.mine_counter(top_frame)
        self.create_new_game_button(top_frame, grid, board)
        self.create_time_counter(top_frame)
        return top_frame


    def mine_counter(self, top_frame):
        mine_counter_str = StringVar()
        def update_mines():
            mine_counter_str.set(model.REMAINING_MINES)
            top_frame.after(100, update_mines)
        update_mines()

        mines_counter = Label(top_frame, height=1, width=4, bg="#EA7CA1", textvariable=mine_counter_str)
        mines_counter.grid(row=0, column=0, padx=5, sticky=W)


    def create_new_game_button(self, top_frame, grid, board):
        def _start_new_game(self, g=grid, b=board):
            self.controller.start_new_game(grid, board)

        newgame_button = Button( top_frame, bd=1, width=15, text="New game",
                                    command=_start_new_game, bg="#EA7CA1")
        newgame_button.grid(row=0, column=1, padx=0, sticky=E)


    def create_time_counter(self, top_frame):
        time_counter_str = StringVar()

        def update_time_counter():
            time_counter_str.set(int((time.time() - model.INIT_TIME)//1))
            top_frame.after(100, update_time_counter)
        update_time_counter()

        time_counter = Label(top_frame, height=1, width=4, bg='#EA7CA1', textvariable=time_counter_str)
        time_counter.grid(row=0, column=4, padx=5, sticky=E)
