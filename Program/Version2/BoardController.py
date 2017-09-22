import tkinter as tk
import sys
import time

class BoardController:
    def __init__(self, model):
        self.model = model

    def left_handler(self, i, j):
        self.model.toggle_btn(i, j)

    def right_handler(self, i, j):
        self.model.flag_btn(i, j)


