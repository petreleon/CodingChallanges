from parse import parse
from operator import methodcaller
file_opened = open("input", 'r')
lines = file_opened.read().splitlines()
# lines.append('')
currentPosition = [0, 0]
dictOfComands = {
    "N":(1, 0),
    "S":(-1,0),
    "E":(0,1),
    "W":(0,-1)
}
translateCommands = {
    ("N", "F"):"N",
    ("S", "F"):"S",
    ("E", "F"):"E",
    ("W", "F"):"W",
    ("N", "L"):"W",
    ("S", "L"):"E",
    ("E", "L"):"N",
    ("W", "L"):"S",
    ("N", "R"):"E",
    ("S", "R"):"W",
    ("E", "R"):"S",
    ("W", "R"):"N",
}

currentDirection = "E"

for index, line in enumerate(lines):
    direction, number = line[:1], int(line[1:]) 
    if direction not in dictOfComands and direction != "F":
        for i in range(number//90):
            currentDirection = translateCommands[(currentDirection, direction)]
    if direction == "F":
        direction = currentDirection
    if direction in dictOfComands:
        toAdd = list(iterated * number for iterated in dictOfComands[direction])
        currentPosition = list(toAdd[index_] + iterated for index_, iterated in enumerate(currentPosition))

print(abs(currentPosition[0])+abs(currentPosition[1]))
