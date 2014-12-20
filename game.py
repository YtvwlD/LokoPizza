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
		self.animations = []
	
	def start(self):
		self.running = True
		pizno = 0
		while (self.running): #unsere Hauptschleife
			self.animate()
			self.lesen()
			self.lokomotive.move()
			self.lokomotive.display()
			for Schiene in self.schienen:
				Schiene.zeit()
			if self.level:
				if pizno > 100:
					self.animations.append(pizzanone(self))
					pizno = 0
				else:
					pizno += 10 * self.level
				sleep(0.0025 * (100 / self.level))
			else:
				sleep(0.125)
	
	def animate(self):
		_animations = []
		for generator in self.animations:
			try:
				next(generator)
			except StopIteration:
				pass
			else:
				_animations.append(generator)
		self.animations = _animations

	def stop(self):
		self.running = False
			
	
	def lesen(self):
		self.lokopizza.screen.nodelay(1)
		if self.level:
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
							self.animations.append(specialfx.explosion(y+1, x+1, self))
		else:
			try:
				wahl = self.lokopizza.screen.getkey()
			except curses.error: #nichts gelesen
				return
			if wahl == "s":
				self.lokopizza.loadLevel(1)
			elif wahl == "o":
				self.lokopizza.screen.addstr(24, 1, "This is currently not possible yet. Sorry.")
				#TODO: Tutorial
			elif wahl == "l":
				self.lokopizza.screen.addstr(24, 1, "Please type your level number. (0 to abort.)")
				self.lokopizza.screen.clrtoeol()
				self.lokopizza.screen.refresh()
				while(True):
					try:
						level = int(self.lokopizza.screen.getkey())
						break
					except curses.error:
						continue
					except ValueError:
						self.lokopizza.screen.addstr(24, 1, "That was no number. Please try again.")
						self.lokopizza.screen.refresh()
						continue
				self.lokopizza.loadLevel(level)
			elif wahl == "e" or wahl == "q":
				self.lokopizza.quit()
			else:
				self.lokopizza.screen.addstr(24, 1, "Please try again.")
				self.lokopizza.screen.clrtoeol()
		self.lokopizza.screen.refresh()
