import random
import curses
import specialfx
import schienen

def pizzanone(game):
	screen = game.lokopizza.screen
	
	# Mache den Cursor unsichtbar, weil sichtbar haesslich
	curses.curs_set(0)
	# Setze while schleife auf True
	keeprunning = True
	
	# Hier faengt die while an, in der die pizza nach unten geflogen kommt
	while(keeprunning):
		randy = random.randint(0, 22)
		randx = random.randint(0, 78)

		# Suche nach Koordinaten, wo randy und randx eine # sind
		if screen.instr(randy, randx, 1) == "#":
			screen.move(24, 30)
			def suche(newy, newx):
				ergebnisgefunden = False
				searchx = newx
				searchy = newy
				koordlist = []

				while not ergebnisgefunden:
					#newy2 = None
					#newx2 = None
					#newx1 = None
					#newy1 = None

					if (searchy, searchx) not in koordlist:
						koordlist.append((searchy, searchx))

					for char in ["X", "^", ">", "v", "<", "|", "_"]: #Ende der Suche: Weichen, Start, Ziel
						newy1, newx1 = game.lokomotive.char_which_direction(searchy, searchx, char)
						if newy1 and newx1:
							return True
							#newy2 = newy1
							#newx2 = newx2
					#if newy2 and newx2:
					#	print str(searchx)+str(searchy)
					#	return True

					newy1, newx1 = game.lokomotive.char_which_direction(searchy, searchx, "#")
					if newy1 and newx1:
						if (newy1, newx1) not in koordlist:
							#print str(searchx)+str(searchy)
							searchx = newx1
							searchy = newy1

							continue
						else:
							pass #print ("Schon gewesen: {} {}".format(newy1, newx1))

					for char in game.lokomotive.chars:
						newy1, newx1 = game.lokomotive.char_which_direction(searchy, searchx, char)
						if newy1 and newx1:
							return True
							#newy2 = newy1
							#newx2 = newx2
							#break
					#if newy2 and newx2:
					#	return False

			if suche(randy, randx):
				# Wenn eins gefunden wurde, hoert die schleife auf und keeprunning wird false
				keeprunning = False
				# Damit die Pizza runterfallen kann wird fally = 0 gesetzt
				fally = 0
				oldchar = None

				# Waehrend fally nicht randy ist, soll die Pizza in Richtung der Schiene fallen
				while(fally != randy):
					if oldchar:
						screen.addstr(fally, randx, oldchar)
					oldchar = screen.instr(fally+1, randx)
					screen.addstr(fally+1, randx, "Q")
					screen.refresh()
					yield None
					fally += 1

				# Und bei fally <= randy wird die Schiene plus Pizza entfernt und special effects sollen danach in x form um die einschlagsstelle auftauchen und wieder verschwinden
				if(fally <= randy):
					game.animations.append(specialfx.explosion(fally, randx, game))
					game.schienen.append(schienen.Schiene(fally, randx, game, "#"))
