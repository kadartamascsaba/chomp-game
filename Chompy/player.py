import numpy as np

"""
Player interface
"""
class Player:

	def move(self, x, y, board):
		raise NotImplementedError("Should have implemented the move function!")

"""
Human class which implements the Player interface
"""
class Human(Player):

	def move(self, x, y, board):
		board_table = board.get_board()

		for i in xrange(0, (board.height - y)):
			board_table[i][x:board.width].fill(1)

		board.set_board(board_table)


"""
AI class which implements the Player interface
"""
class AI(Player):

	def move(self, x, y, board):
		pass
