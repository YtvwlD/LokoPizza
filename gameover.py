from mapread import mapread
from time import sleep
import specialfx
import random
from threading import Thread
from schienen import Schiene

def gameover(lokopizza):
	mapread(lokopizza, "gameover.txt")
	lokopizza.screen.refresh()
	
	while(True):
		randy = random.randint(2, 22)
		randx = random.randint(2, 78)
		specialfx.explosion(randy, randx, lokopizza)
		char = lokopizza.screen.instr(randy, randx, 1)
		lokopizza.schienen.append(Schiene(randy, randx, lokopizza, char))
