from time import sleep

class Schiene:
	
	def __init__(self, y, x, game, character):
		self.x = x
		self.y = y
		self.character = character
		self.game = game
		self.counter = 0
		
	def zeit(self):
		self.counter += 1
		
		if (self.counter >= 10):
			self.game.lokopizza.screen.addstr(self.y, self.x, self.character)
			self.game.schienen.remove(self)
