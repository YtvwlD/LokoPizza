from time import sleep

class Schiene:

    def __init__(self, y, x, lokopizza, character):
        self.x = x
        self.y = y
        self.character = character
        self.lokopizza = lokopizza
        self.counter = 0

    def zeit(self):
        self.counter += 1

        if (self.counter >= 10):
            self.lokopizza.screen.addstr(self.y, self.x, self.character)
            self.lokopizza.schienen.remove(self)