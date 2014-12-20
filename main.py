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
		
		Game(self, 1).start()
		

if __name__ == "__main__":
	lokopizza = LokoPizza()
	curses.endwin()
