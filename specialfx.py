from time import sleep


def explosion(y, x, lokopizza):
    lokopizza.screen.addstr(y, x, " ")
    lokopizza.screen.move(24, 79)
    lokopizza.screen.refresh()
    sleep(0.3)
    
    oldchar1 = lokopizza.screen.instr(y+1, x+1)
    oldchar2 = lokopizza.screen.instr(y-1, x+1)
    oldchar3 = lokopizza.screen.instr(y-1, x-1)
    oldchar4 = lokopizza.screen.instr(y+1, x-1)
    
    lokopizza.screen.addstr(y+1, x+1, "*")
    lokopizza.screen.addstr(y-1, x+1, "*")
    lokopizza.screen.addstr(y-1, x-1, "*")
    lokopizza.screen.addstr(y+1, x-1, "*")
    lokopizza.screen.refresh()
    lokopizza.screen.move(24, 79)
    sleep(0.2)
    
    oldchar11 = lokopizza.screen.instr(y+2, x+2)
    oldchar22 = lokopizza.screen.instr(y-2, x+2)
    oldchar33 = lokopizza.screen.instr(y-2, x-2)
    oldchar44 = lokopizza.screen.instr(y+2, x-2)
    
    lokopizza.screen.addstr(y+2, x+2, "*")
    lokopizza.screen.addstr(y-2, x+2, "*")
    lokopizza.screen.addstr(y-2, x-2, "*")
    lokopizza.screen.addstr(y+2, x-2, "*")
    lokopizza.screen.refresh()
    lokopizza.screen.move(24, 79)
    sleep(0.1)
    
    lokopizza.screen.addstr(y+1, x+1, oldchar1)
    lokopizza.screen.addstr(y-1, x+1, oldchar2)
    lokopizza.screen.addstr(y-1, x-1, oldchar3)
    lokopizza.screen.addstr(y+1, x-1, oldchar4)
    lokopizza.screen.refresh()
    lokopizza.screen.move(24, 79)
    sleep(0.1)
    
    lokopizza.screen.addstr(y+2, x+2, oldchar11)
    lokopizza.screen.addstr(y-2, x+2, oldchar22)
    lokopizza.screen.addstr(y-2, x-2, oldchar33)
    lokopizza.screen.addstr(y+2, x-2, oldchar44)
    lokopizza.screen.refresh()
    lokopizza.screen.move(24, 79)