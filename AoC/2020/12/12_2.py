from parse import parse
from operator import methodcaller
file_opened = open("input", 'r')
lines = file_opened.read().splitlines()
# lines.append('')
currentPosition = [0, 0]
waypoint = [1, 10]

def rotateRight(number):
    global waypoint
    for _ in range(number//90):
        waypoint = [- waypoint[1], waypoint[0] ]
def rotateLeft(number):
    global waypoint
    for _ in range(number//90):
        waypoint = [ waypoint[1], - waypoint[0] ]

def moveFoward(number):
    global waypoint, currentPosition
    currentPosition = [iterated + waypoint[index] * number for index, iterated in enumerate(currentPosition)]

dictOfComands = {
    "N":(1, 0),
    "S":(-1,0),
    "E":(0,1),
    "W":(0,-1)
}
translateCommands = {
    "R":rotateRight,
    "L":rotateLeft,
    "F":moveFoward 
}

currentDirection = "E"

for index, line in enumerate(lines):
    direction, number = line[:1], int(line[1:]) 
    if direction in translateCommands:
        translateCommands[direction](number)
    if direction in dictOfComands:
        command = dictOfComands[direction]
        waypoint = [iterated + command[index_] * number for index_, iterated in enumerate(waypoint)]
    
    
print(abs(currentPosition[0])+abs(currentPosition[1]))
