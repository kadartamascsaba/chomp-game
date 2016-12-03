import numpy as np

"""
Model class for Chomp Game
"""
class Board:

	"""
	Constuctor
	"""
	def __init__(self, n, m):

		# Size of board
		self.width       = n
		self.height      = m
		
		# Initialize board matix
		self.board       = np.zeros((self.height, self.width), dtype=np.int)
		self.board[(self.height - 1)][0] = -1

	"""
	Getter and setter functions
	"""
	def get_board(self):
		return self.board

	def set_board(self, board):
		self.board = board
