from mapread import mapread
from pizzanone import pizzanone
from lokomotive import Lokomotive
import specialfx
import curses
from time import sleep

class Game:
	def __init__(self, lokopizza, level):
		self.level = level
		self.lokopizza = lokopizza
		mapread(self, "map{}.txt".format(level))
		self.lokomotive = Lokomotive(self)
		self.lokopizza.screen.refresh()
		self.schienen = []
	
	def start(self):
		self.running = True
		pizno = 0
		while (self.running): #unsere Hauptschleife
			self.lesen()
			self.lokomotive.move()
			self.lokomotive.display()
			for Schiene in self.schienen:
				Schiene.zeit()
			if pizno > (100 / self.level):
				pizzanone(self)
				pizno = 0
			else:
				pizno += 100
			sleep(0.25)
	
	def stop(self):
		self.running = False
			
	
	def lesen(self):
		self.lokopizza.screen.nodelay(1)
		try:
			weiche = int(self.lokopizza.screen.getkey())
		except curses.error: #nichts gelesen
			return
		except ValueError:
			return
		while (True):
			richtung = self.lokopizza.screen.getch()
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
				if str(weiche) == self.lokopizza.screen.instr(y,x,1):
					if self.lokopizza.screen.instr(y+1, x+1, 1) in ["X", "^", ">", "v", "<"]:
						self.lokopizza.screen.addstr(y+1, x+1, pfeil)
					else:
						specialfx.explosion(y+1, x+1, self)
		self.lokopizza.screen.refresh()
