#!/usr/bin/env python
import curses
import sys
from game import Game

class LokoPizza:
	def __init__(self):
		self.screen = curses.initscr()
		self.screen.clear()
		self.screen.refresh()
		curses.noecho()
		self.game = Game(self, 0)
		self.game.start()
	
	def nextLevel(self):
		level = self.game.level
		if level:
			level += 1
		self.loadLevel(level)
	
	def loadLevel(self, level):
		self.screen.clear()
		self.game.stop()
		self.game = Game(self, level)
		self.game.start()
	
	def quit(self):
		curses.endwin()
		sys.exit(0)

if __name__ == "__main__":
	lokopizza = LokoPizza()
