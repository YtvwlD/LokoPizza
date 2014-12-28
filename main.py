#!/usr/bin/env python
import curses
import sys
from game import Game
from music import Music


class LokoPizza:
	def __init__(self):
		if len(sys.argv) != 2:
			print ("Please select the music to play via sys.arvg[1].")
			print ("None, bgm, train or NootNoot.")
			sys.exit(1)
		self.music = Music(sys.argv[1])
		self.screen = curses.initscr()
		self.screen.clear()
		self.screen.refresh()
		self.music.start()
		self.mapstr = "map{}.txt"
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
		self.music.reset()
		self.game.stop()
		try:
			self.game = Game(self, level)
			self.game.start()
		except IOError:
			self.mapstr = "map{}.txt"
			self.loadLevel(0)
	
	def quit(self):
		self.music.keeprunning = False
		curses.endwin()
		sys.exit(0)

if __name__ == "__main__":
	lokopizza = LokoPizza()
