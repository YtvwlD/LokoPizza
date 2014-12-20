import random
import curses
from time import sleep

def pizzanone(lokopizza):
    curses.curs_set(0)
    keeprunning = True

    while(keeprunning):
        randy = random.randint(0, 24)
        randx = random.randint(0, 80)

        if lokopizza.screen.instr(randy, randx, 1) == "#":
            keeprunning = False
            fally = 0
            oldchar = None
            while(fally != randy):
                if oldchar:
                    lokopizza.screen.addstr(fally, randx, oldchar)
                oldchar = lokopizza.screen.instr(fally+1, randx)
                lokopizza.screen.addstr(fally+1, randx, "Q")
                lokopizza.screen.move(24, 79)
                lokopizza.screen.refresh()
                sleep(0.1)
                fally += 1
