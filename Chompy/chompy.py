import random

from Tkinter import Tk
from gui import ChompUI

from board import Board
from player import *

# Chompy Game class
class Game:
	def __init__(self):
		self.blocked = True

	def set_ui(self, ui):
		self.ui = ui

	def step(self, x, y):
		if not self.blocked:
			if not self.player1.move(self.board, x, y):
				self.ui.invalid_move()
				return

			self.ui.update(self.board.get_board())
			if self.player1.is_finished(self.board.get_board()):
				self.ui.game_over("You")
				return

			self.blocked = True

			self.player2.move(self.board)

			self.ui.update(self.board.get_board())
			if self.player2.is_finished(self.board.get_board()):
				self.ui.game_over("AI")
				return

			self.blocked = False

	# Starting game
	def start_game(self, width, height):
		self.board = Board(width, height)

		self.player1 = Human(height, width)
		self.player2 = AI(height, width)

		# If the random number is smaller than 0.5 then AI player start the game
		if (random.uniform(0, 1) <= 0.5):
			self.player2.move(self.board)
			self.ui.update(self.board.get_board())
		self.blocked = False

# Main function
if __name__ == '__main__':
	# Make a game and a UI objects
	game = Game()
	
	root = Tk()
	chomp_ui = ChompUI(root, game)
	
	game.set_ui(chomp_ui)

	root.mainloop()
