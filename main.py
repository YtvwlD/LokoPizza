#!/usr/bin/env python
import curses
import sys
from argparse import ArgumentParser
from game import Game
from music import Music


class LokoPizza:
	def __init__(self, sound="None"):
		self.music = Music(sound)
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
	argparse = ArgumentParser()
	argparse.add_argument("sound", help="which sounds to make (can be: \"None\", \"bgm\", \"train\" or \"NootNoot\")")
	args = argparse.parse_args()
	lokopizza = LokoPizza(sound=args.sound)
