#!/usr/bin/env python
import curses
from time import sleep
import gameover
from game import Game

class LokoPizza:
	def __init__(self):
		self.screen = curses.initscr()
		self.screen.clear()
		self.screen.refresh()
		curses.noecho()
		#TODO: Menue
		self.game = Game(self, 1)
		self.game.start()
	
	def nextLevel(self):
		self.screen.clear()
		level = self.game.level + 1
		self.game.stop()
		self.game = Game(self, level)
		self.game.start()

if __name__ == "__main__":
	lokopizza = LokoPizza()
	curses.endwin()
