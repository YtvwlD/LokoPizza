def mapread(lokopizza):
    map = open("map1.txt", "r")

    tmpstr = map.read()
    tmparray = tmpstr.splitlines()

    y = 0

    for line in tmparray:
        x = 0
        for character in line:
            lokopizza.screen.addstr(y, x, character)
            x += 1
        y += 1