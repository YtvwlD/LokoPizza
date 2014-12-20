#!/usr/bin/env python
import curses
from time import sleep
from mapread import mapread
from pizzanone import pizzanone
from lokomotive import Lokomotive

class LokoPizza:
	def __init__(self):
		self.screen = curses.initscr()
		self.screen.clear()
		self.screen.refresh()
		
		mapread(self, "map1.txt")
		self.lokomotive = Lokomotive(self)
		self.screen.refresh()
		pizzanone(self)
		
		while (True): #unsere Hauptschleife
			self.lesen()
			self.lokomotive.move()
			self.lokomotive.display()
			sleep(0.25)
	
	def lesen(self):
		self.screen.nodelay(1)
		try:
			weiche = int(self.screen.getkey())
		except curses.error: #nichts gelesen
			return
		except ValueError:
			return
		while (True):
			richtung = self.screen.getch()
			if richtung != -1: #kein Zeichen
				if richtung != 27: #ESC
					if richtung != 91: #[
						break
		if richtung == 65: #curses.KEY_UP
			pfeil = "^"
		elif richtung == 67: #curses.KEY_RIGHT
			pfeil = ">"
		elif richtung == 66: #curses.KEY_DOWN
			pfeil = "v"
		elif richtung == 68: #curses.KEY_LEFT
			pfeil = "<"
		else:
			return
		for y in range(25):
			for x in range(80):
				if str(weiche) == self.screen.instr(y,x,1):
					self.screen.addstr(y+1, x+1, pfeil)
		self.screen.refresh()

if __name__ == "__main__":
	lokopizza = LokoPizza()
	curses.endwin()
