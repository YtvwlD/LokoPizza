def mapread(game, filename):
    map = open(filename, "r")

    tmpstr = map.read()
    tmparray = tmpstr.splitlines()

    y = 0

    for line in tmparray:
        x = 0
        for character in line:
            game.lokopizza.screen.addstr(y, x, character)
            x += 1
        y += 1