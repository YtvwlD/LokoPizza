#!/usr/bin/env python
import curses
import sys
from argparse import ArgumentParser
from time import sleep
from game import Game
from music import Music


class LokoPizza:
	def __init__(self, sound="None", soundout="pulse"):
		self.music = Music(sound, soundout)
		sleep(0.25)
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
	argparse.add_argument("--soundout", help="how to output the sound (can be: \"pulse\" or \"alsa\")", default="pulse")
	args = argparse.parse_args()
	lokopizza = LokoPizza(sound=args.sound, soundout=args.soundout)
