import math
from Tkinter import *

WINDOW_SIZE = 360000
MAX_SIZE_OF_BOARD = 30
DEFAULT_WIDTH = 10
DEFAULT_HEIGHT = 4

class ChompUI:
    def __init__(self, master):
        self.master = master

        self.master.title("Chomp Game")
        self.master.geometry("800x600")
        self.master.resizable(width=False, height=False)

        self.width_string_var = StringVar()
        self.height_string_var = StringVar()

        self.width = DEFAULT_WIDTH
        self.height = DEFAULT_HEIGHT

        self.title_label = Label(self.master, text="Chomp Game")
        self.title_label.pack()

        self.size_label = Label(self.master, text="Please add size of Chocolate")
        self.size_label.pack()

        self.width_label = Label(self.master, text="Width")
        self.width_label.pack()
        self.width_entry = Entry(self.master, textvariable=self.width_string_var)
        self.width_entry.pack()

        self.height_label = Label(self.master, text="Height")
        self.height_label.pack()
        self.height_entry = Entry(self.master, textvariable=self.height_string_var)
        self.height_entry.pack()

        self.start_button = Button(master, text="Start", command=self.start_game)
        self.start_button.pack()

        self.close_button = Button(master, text="Close", command=self.master.quit)
        self.close_button.pack()

    def start_game(self):
        if self.is_valid():
            print "Starting game..."
            self.clear_frame()
            self.master.configure(background="sienna")
            self.create_game_board()

    def create_game_board(self):
        print "Creating chocolate..."
        button_width = int(800 / self.width) - 10
        button_height = int(600 / self.height) - 10

        for i in xrange(self.height):
            for j in xrange(self.width):
                frame = Frame(self.master, width=button_width, height=button_height)
                frame.rowconfigure(0, weight=1)
                frame.columnconfigure(0, weight=1)
                frame.grid_propagate(0)

                if i == j == 0:
                    chocolate_bar = Button(frame, width=button_width, height=button_height, bg="Orangered4", command=self.play)
                else:
                    chocolate_bar = Button(frame, width=button_width, height=button_height, bg="saddle brown", command=self.play)

                frame.grid(row=i, column=j, padx=5, pady=5)
                chocolate_bar.grid(sticky="NWSE")

    def play(self):
        print "Say Hello!"

    def clear_frame(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def is_valid(self):
        try:
            self.width = int(self.width_string_var.get())
            self.height = int(self.height_string_var.get())
        except ValueError:
            return False
        if self.width in xrange(0, MAX_SIZE_OF_BOARD) and self.height in xrange(0, MAX_SIZE_OF_BOARD):
            return True
        return False
