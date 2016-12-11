import numpy as np

from copy import copy

# Declaring infinity
inf = float('inf') 

"""
Player interface
"""
class Player:

	def __init__(self, row, column):
		self.row = row
		self.column = column
		self.search_depth = 5

		self.states = []
		self.moves = [()]

	# This function check the game is finished or not
	def is_finished(self, board):
		return not np.any(board.flatten()==0)

	# This function return a list with legal moves. For example: [(0, 1), ...,(4, 5), ...,(5, 5)]
	def get_possible_moves(self):
		possible_moves = []

		for column in xrange(self.column):
			for row in xrange(self.row):
				if self.states[-1][row][column] == 0:
					possible_moves.append((row, column))

		return possible_moves

	def move(self, board, x=0, y=0):
		raise NotImplementedError("Should have implemented the move function!")

"""
Human class which implements the Player interface
"""
class Human(Player):

	# Humna move function
	def move(self, board, x, y):
		self.states.append(board.get_board())

		# If the human player move is possible play it
		if (x, y) in self.get_possible_moves():
			board_table = board.get_board()

			for i in xrange(x, board.height):
				self.states[-1][i][y:board.width].fill(1)

			board.set_board(self.states[-1])
			self.states = self.states[:-1]
			print "INFO - Human player moved: " + str(x) + ", " + str(y)
			return True
		# The human player move is impossible
		else:
			self.states = self.states[:-1]
			return False


"""
AI class which implements the Player interface
"""
class AI(Player):

	# This function make a move on board
	def do_step(self, move):
		(x, y) = move

		self.moves.append(move)
		board = copy(self.states[-1])

		for i in xrange(x, self.row):
			board[i][y:self.column].fill(1)

		self.states.append(board)

	# This function delete last move
	def undo_step(self, move):
		self.moves = self.moves[:-1]
		self.states = self.states[:-1]

	# Evaluation function for alpa beta puring
	def evaluate(self):
		win_value = 2 + self.column * self.row - len(self.moves)

		if self.is_finished(self.states[-1]):
			return - win_value
		else:
			return 0

	# Alpha beta puring function
	def alphabeta_puring(self, depth, alpha, beta):
		if depth >= self.search_depth or self.is_finished(self.states[-1]):
			value = self.evaluate()
			return value

		possible_moves = self.get_possible_moves()
		for i in xrange(len(possible_moves)):

			self.do_step(possible_moves[i])
			value = (-1) * self.alphabeta_puring(depth + 1, -beta, -alpha)
			self.undo_step(possible_moves[i])

			if value >= beta:
				return value

			if value > alpha:
				alpha = value

		return alpha

	# Return the best move, which found with alfabeta puring.
	def get_move(self):
		beta = inf
		alpha = -inf
		alpha_move = None

		for move in self.get_possible_moves():

			self.do_step(move)
			value = - self.alphabeta_puring(1, -beta, -alpha)
			self.undo_step(move)

			if value > alpha:
				(alpha, alpha_move) = (value, move)

		return alpha_move

	# AI move function
	def move(self, board):
		self.board_table = board.get_board()
		self.states.append(self.board_table)
		(x, y) = self.get_move()
		print "INFO - AI player moved: " + str(x) + ", " + str(y)

		for i in xrange(x, board.height):
			self.board_table[i][y:board.width].fill(1)

		board.set_board(self.board_table)
		self.states = self.states[:-1]
