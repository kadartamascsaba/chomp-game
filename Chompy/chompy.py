from Tkinter import Tk
from gui import ChompUI
from game import Game

if __name__ == '__main__':
	game = Game()
	root = Tk()
	chomp_ui = ChompUI(root, game)

	root.mainloop()
