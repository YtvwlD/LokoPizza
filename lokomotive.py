class Lokomotive():
	def __init__(self, lokopizza):
		self.lokopizza = lokopizza
		self.oldchars = []
		for y in range(25):
			self.oldchars.append([])
			for x in range(80):
				self.oldchars[y].append(None)
				if self.lokopizza.screen.instr(y,x,3) == "|_|": #start
					self.x = x+2
					self.y = y

	def move(self):
		self.x += 1
		self.display()
	
	def display(self):
		screen = self.lokopizza.screen
		chars = "Lokomotive"
		def old_char_which_direction(y, x, old):
			if screen.instr(y, x-1, 1) == old: #links
				return (y, x-1)
			elif screen.instr(y-1, x, 1) == old: #oben
				return (y-1, x)
			elif screen.instr(y, x+1, 1) == old: #rechts
				return (y, x+1)
			elif screen.instr(y+1, x, 1) == old: #unten
				return (y+1, x)
			else:
				return (None, None)
		
		def recursion(y, x, charidx):
			newy, newx = old_char_which_direction(y, x, chars[-charidx])
			if newy and newx:
				try:
					screen.addstr(newy, newx, chars[-charidx-1])
					recursion(newy, newx, charidx + 1)
				except IndexError: #Ende - jetzt kommt wieder die urspruengliche Strecke
					screen.addstr(newy, newx, self.oldchars[newy][newx])
		recursion(self.y, self.x, 1)
		self.oldchars[self.y][self.x] = screen.instr(self.y, self.x, 1)
		screen.addstr(self.y, self.x, chars[-1])
		
		self.lokopizza.screen.refresh()
