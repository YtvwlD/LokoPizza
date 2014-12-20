#!/usr/bin/env python
import locale
import curses
from time import sleep
from mapread import mapread
from pizzanone import pizzanone

class LokoPizza:
	def __init__(self):
		self.screen = curses.initscr()
		self.screen.clear()
		#self.screen.border(0)
		self.screen.refresh()
		
		mapread(self)
		self.screen.refresh()
		pizzanone(self)
		
		while (True): #unsere Hauptschleife
			self.lesen()
	
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
			pfeil = unichr(8593)
		elif richtung == 67: #curses.KEY_RIGHT
			pfeil = unichr(8594)
		elif richtung == 66: #curses.KEY_DOWN
			pfeil = unichr(8595)
		elif richtung == 68: #curses.KEY_LEFT
			pfeil = unichr(8592)
		else:
			return
		for y in range(25):
			for x in range(80):
				if str(weiche) == self.screen.instr(y,x,1):
					self.screen.addstr(y+1, x+1, unicode(pfeil).encode(code))
		self.screen.refresh()

if __name__ == "__main__":
	locale.setlocale(locale.LC_ALL, '')
	code = locale.getpreferredencoding()
	lokopizza = LokoPizza()
	curses.endwin()
