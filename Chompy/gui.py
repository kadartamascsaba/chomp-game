from Tkinter import *
from tkMessageBox import *

# Default constants
WINDOW_SIZE = 360000
MAX_SIZE_OF_BOARD = 15
MAX_DEPTH = 20

# UI class for Chomp Game
class ChompUI:

	# Constructor
	def __init__(self, master, game):
		self.master = master

		self.game = game

		self.master.title("Chomp Game")
		self.master.geometry("800x600")
		self.master.resizable(width=False, height=False)

		self.width_string_var = StringVar()
		self.height_string_var = StringVar()
		self.depth_string_var = StringVar()

		frame = Frame(self.master, width=400, height=100)
		frame.rowconfigure(0, weight=1)
		frame.columnconfigure(0, weight=1)
		frame.grid_propagate(0)

		self.title_label = Label(frame, text="Chomp Game", font=("Helvetica", 32))
		self.title_label.grid(row=0,column=0)

		self.size_label = Label(frame, text="Please add the parameters", font=("Helvetica", 16))
		self.size_label.grid(row=1, column=0)

		frame.pack()

		frame = Frame(self.master, width=250, height=200)
		frame.rowconfigure(0, weight=1)
		frame.columnconfigure(0, weight=1)
		frame.grid_propagate(0)

		self.width_label = Label(frame, text="Width")
		self.width_label.grid(row=2, column=0)
		self.width_entry = Entry(frame, textvariable=self.width_string_var)
		self.width_entry.grid(row=2, column=1)

		self.height_label = Label(frame, text="Height")
		self.height_label.grid(row=3, column=0)
		self.height_entry = Entry(frame, textvariable=self.height_string_var)
		self.height_entry.grid(row=3, column=1)

		self.depth_label = Label(frame, text="Depth")
		self.depth_label.grid(row=4, column=0)
		self.depth_entry = Entry(frame, textvariable=self.depth_string_var)
		self.depth_entry.grid(row=4, column=1)

		self.start_button = Button(frame, text="Start", command=self.initialize_UI)
		self.start_button.grid(row=5, column=0)

		self.close_button = Button(frame, text="Close", command=self.master.quit)
		self.close_button.grid(row=5, column=1)

		frame.pack()

	# Initialize UI elements
	def initialize_UI(self):
		if self.is_valid():
			print "INFO - Initizalize UI for game..."
			self.clear_frame()
			self.board = []
			self.master.configure(background="sienna")
			self.create_game_board()
			self.game.start_game(self.width, self.height, self.depth)
		else:
			showinfo("Info", "Bad parameters")

	# Creating the UI board
	def create_game_board(self):
		print "INFO - Creating chocolate..."
		button_width = int(800 / self.width) - 10
		button_height = int(600 / self.height) - 10

		for i in xrange(self.height):
			chocolate_row = []
			for j in xrange(self.width):
				frame = Frame(self.master, width=button_width, height=button_height)
				frame.rowconfigure(0, weight=1)
				frame.columnconfigure(0, weight=1)
				frame.grid_propagate(0)

				if (i == 0) and (j == 0):
					chocolate_bar = Button(frame, width=button_width, height=button_height, bg="Orangered4", command=lambda i=i,j=j: self.move(i,j))
				else:
					chocolate_bar = Button(frame, width=button_width, height=button_height, bg="saddle brown", command=lambda i=i,j=j: self.move(i,j))

				frame.grid(row=i, column=j, padx=5, pady=5)
				chocolate_bar.grid(sticky="NWSE")
				chocolate_row.append(chocolate_bar)
			self.board.append(chocolate_row)

	# Update frame buttons with board model
	def update(self, board):
		for i in xrange(board.shape[0]):
			for j in xrange(board.shape[1]):
				if (board[i][j] == 1):
					self.board[i][j].configure(bg="black")
				elif (board[i][j] == 0):
					self.board[i][j].configure(bg="saddle brown")
				else:
					self.board[i][j].configure(bg="Orangered4")

	def game_over(self, who):
		print "INFO - Game Over " + who + " won this game..."
		if askyesno('Game Over', who + ' won this game. Do you want to play again?'):
			self.initialize_UI()
		else:
			self.master.quit()

	def move(self, i, j):
		self.game.step(i, j)

	def invalid_move(self):
		showinfo("Info", "This move is invalid, please make antoher one")

	# Clear all item from frame
	def clear_frame(self):
		print "INFO - Clear frame..."
		for widget in self.master.winfo_children():
			widget.destroy()

	# This function check the parameters
	def is_valid(self):
		print "INFO - Validity checking..."
		try:
			self.width = int(self.width_string_var.get())
			self.height = int(self.height_string_var.get())
			self.depth = int(self.depth_string_var.get())
		except ValueError:
			return False
		if self.width in xrange(0, MAX_SIZE_OF_BOARD) and self.height in xrange(0, MAX_SIZE_OF_BOARD) and self.depth in xrange(0, MAX_DEPTH):
			return True
		return False
