def explosion(y, x, game):
	game.lokopizza.music.explosion()
	screen = game.lokopizza.screen
	screen.addstr(y, x, " ")
	screen.refresh()
	yield None
	yield None
	yield None
	
	oldchar1 = screen.instr(y+1, x+1)
	oldchar2 = screen.instr(y-1, x+1)
	oldchar3 = screen.instr(y-1, x-1)
	oldchar4 = screen.instr(y+1, x-1)
	
	screen.addstr(y+1, x+1, "*")
	screen.addstr(y-1, x+1, "*")
	screen.addstr(y-1, x-1, "*")
	screen.addstr(y+1, x-1, "*")
	screen.refresh()
	yield None
	yield None
	
	oldchar11 = screen.instr(y+2, x+2)
	oldchar22 = screen.instr(y-2, x+2)
	oldchar33 = screen.instr(y-2, x-2)
	oldchar44 = screen.instr(y+2, x-2)
	
	screen.addstr(y+2, x+2, "*")
	screen.addstr(y-2, x+2, "*")
	screen.addstr(y-2, x-2, "*")
	screen.addstr(y+2, x-2, "*")
	screen.refresh()
	yield None
	
	screen.addstr(y+1, x+1, oldchar1)
	screen.addstr(y-1, x+1, oldchar2)
	screen.addstr(y-1, x-1, oldchar3)
	screen.addstr(y+1, x-1, oldchar4)
	screen.refresh()
	yield None
	
	screen.addstr(y+2, x+2, oldchar11)
	screen.addstr(y-2, x+2, oldchar22)
	screen.addstr(y-2, x-2, oldchar33)
	screen.addstr(y+2, x-2, oldchar44)
	screen.refresh()
