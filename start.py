#!/usr/bin/env python
import curses
from time import sleep
from mapread import mapread

class LokoPizza:
	def __init__(self):
		self.screen = curses.initscr()
		self.screen.clear()
		self.screen.border(0)
		self.screen.refresh()
		
		mapread(self)
		self.screen.refresh()

if __name__ == "__main__":
		LokoPizza()
		curses.endwin()