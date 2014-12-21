from mapread import mapread
from pizzanone import pizzanone
from lokomotive import Lokomotive
import specialfx
import curses
from time import sleep
from wave import open as waveOpen

class Game:
	def __init__(self, lokopizza, level):
		self.level = level
		self.lokopizza = lokopizza
		mapread(self, "map{}.txt".format(level))
		self.lokomotive = Lokomotive(self)
		self.lokopizza.screen.refresh()
		wave = waveOpen("NootNoot.wav", "rb")
		lokopizza.pa.stdin.write(wave.readframes(1000000000000000))
		lokopizza.pa.stdin.flush()
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
					pizno += 5 * self.level
				sleep(0.002 * (100 / self.level))
			else:
				sleep(0.25)
	
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
				res = self.lokopizza.screen.getkey()
				weiche = int(res)
				for y in range(25):
					for x in range(80):
						if str(weiche) == self.lokopizza.screen.instr(y,x,1):
							self.lokopizza.screen.addstr(y, x, str(weiche),  curses.A_REVERSE)
							self.lokopizza.screen.addstr(y+1, x+1, self.lokopizza.screen.instr(y+1, x+1, 1),  curses.A_REVERSE)
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
								self.lokopizza.screen.addstr(y, x, str(weiche),  curses.A_NORMAL)
								self.lokopizza.screen.addstr(y+1, x+1, self.lokopizza.screen.instr(y+1, x+1, 1),  curses.A_NORMAL)
								return

							if self.lokopizza.screen.instr(y+1, x+1, 1) in ["X", "^", ">", "v", "<"]:
								self.lokopizza.screen.addstr(y+1, x+1, pfeil, curses.A_NORMAL)
							else:
								self.animations.append(specialfx.explosion(y+1, x+1, self))
							self.lokopizza.screen.addstr(y, x, str(weiche),  curses.A_NORMAL)
			except curses.error: #nichts gelesen
				return
			except ValueError:
				if res == "r": #restart
					self.lokopizza.loadLevel(self.level)
				elif res == "\x1b": #ESC
					self.lokopizza.loadLevel(0)
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
						self.lokopizza.screen.addstr(24, 1, "That was no number. Please try again. (0 to abort.)")
						self.lokopizza.screen.refresh()
						continue
				self.lokopizza.loadLevel(level)
			elif wahl == "e" or wahl == "q":
				self.lokopizza.quit()
			else:
				self.lokopizza.screen.addstr(24, 1, "Please try again.")
				self.lokopizza.screen.clrtoeol()
		self.lokopizza.screen.refresh()
