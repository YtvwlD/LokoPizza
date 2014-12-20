import specialfx
from gameover import gameover

class Lokomotive:
	def __init__(self, game):
		self.game = game
		self.screen = self.game.lokopizza.screen
		self.oldchars = []
		for y in range(25):
			self.oldchars.append([])
			for x in range(80):
				self.oldchars[y].append(None)
				if self.screen.instr(y,x,1) == "|": #start
					self.x = x
					self.y = y
	
	def move(self):
		rail = False
		#Behandlung der Weichen:
		if self.oldchars[self.y][self.x] == "^":
			if self.screen.instr(self.y-1, self.x, 1) == "#": #oben
				rail = True
				self.y -= 1
		elif self.oldchars[self.y][self.x] == "<":
			if self.screen.instr(self.y, self.x-1, 1) == "#": #links
				rail = True
				self.x -= 1
		elif self.oldchars[self.y][self.x] == "v":
			if self.screen.instr(self.y+1, self.x, 1) == "#": #unten
				rail = True
				self.y += 1
		elif self.oldchars[self.y][self.x] == ">":
			if self.screen.instr(self.y, self.x+1, 1) == "#": #rechts
				rail = True
				self.x += 1
		elif (None, None) != self.char_which_direction(self.y, self.x, "_"):
			self.game.lokopizza.nextLevel()
		#normale Schienen - oder der Start
		else:
			for char in ["#", "^", ">", "v", "<"]:
				newy, newx = self.char_which_direction(self.y, self.x, char)
				if newy and newx: #Schienen in der Naehe
					rail = True
					self.y = newy
					self.x = newx
					break
		
		if not rail: #Explosion, wenn es keine Schienen gibt
			self.game.animations.append(specialfx.explosion(self.y, self.x, self.game))
			gameover(self.game)
	
	def char_which_direction(self, y, x, char):
		if self.screen.instr(y, x-1, 1) == char: #links
			return (y, x-1)
		elif self.screen.instr(y-1, x, 1) == char: #oben
			return (y-1, x)
		elif self.screen.instr(y, x+1, 1) == char: #rechts
			return (y, x+1)
		elif self.screen.instr(y+1, x, 1) == char: #unten
			return (y+1, x)
		else:
			return (None, None)
	
	def display(self):
		chars = "LOKOMOTIVE"
		
		def recursion(y, x, charidx):
			newy, newx = self.char_which_direction(y, x, chars[-charidx])
			if newy and newx:
				try:
					self.screen.addstr(newy, newx, chars[-charidx-1])
					recursion(newy, newx, charidx + 1)
				except IndexError: #Ende - jetzt kommt wieder die urspruengliche Strecke
					self.screen.addstr(newy, newx, self.oldchars[newy][newx])
		recursion(self.y, self.x, 1)
		self.oldchars[self.y][self.x] = self.screen.instr(self.y, self.x, 1)
		self.screen.addstr(self.y, self.x, chars[-1])
		self.screen.refresh()
