import random
import curses
import specialfx
from time import sleep

def pizzanone(lokopizza):

    # Mache den Cursor unsichtbar, weil sichtbar haesslich
    curses.curs_set(0)
    # Setze while schleife auf True
    keeprunning = True

    # Hier faengt die while an, in der die pizza nach unten geflogen kommt
    while(keeprunning):
        randy = random.randint(0, 22)
        randx = random.randint(0, 78)

        # Suche nach Koordinaten, wo randy und randx eine # sind
        if lokopizza.screen.instr(randy, randx, 1) == "#":
            # Wenn eins gefunden wurde, hoert die schleife auf und keeprunning wird false
            keeprunning = False
            # Damit die Pizza runterfallen kann wird fally = 0 gesetzt
            fally = 0
            oldchar = None

            # Waehrend fally nicht randy ist, soll die Pizza in Richtung der Schiene fallen
            while(fally != randy):
                if oldchar:
                    lokopizza.screen.addstr(fally, randx, oldchar)
                oldchar = lokopizza.screen.instr(fally+1, randx)
                lokopizza.screen.addstr(fally+1, randx, "Q")
                lokopizza.screen.move(24, 79)
                lokopizza.screen.refresh()
                sleep(0.1)
                fally += 1

            # Und bei fally <= randy wird die Schiene plus Pizza entfernt und special effects sollen danach in x form um die einschlagsstelle auftauchen und wieder verschwinden
            if(fally <= randy):
                specialfx.explosion(fally, randx, lokopizza)
