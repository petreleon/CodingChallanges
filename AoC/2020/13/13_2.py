from parse import parse
from operator import methodcaller
from sympy.ntheory.modular import crt

file_opened = open("input", 'r')
lines = file_opened.read().splitlines()
# lines.append('')
time = int(lines[0])
buses = lines[1].split(',')
busIDs = []
for iterated in buses:
    if iterated != 'x':
        busIDs.append([int(iterated), 0])
    if iterated == 'x':
        busIDs[-1][1] += 1
found = False
timeStamp = 0
lcm = busIDs[0][0]

EquationsMod = [busIDs[0][0]]
EquationsEqual = [0]

print("Mod[x,{}]=={}".format(busIDs[0][0], 0), end='')
iterated = 1 + busIDs[0][1]
for index,iteratedID in enumerate(busIDs[1:]):
    print("&& Mod[x,{}]=={}".format(iteratedID[0], (-iterated)%iteratedID[0]), end="")
    EquationsMod.append(iteratedID[0])
    EquationsEqual.append((-iterated)%iteratedID[0])
    iterated += iteratedID[1] + 1
print('')
solution = crt(EquationsMod, EquationsEqual)
print(solution[0])
# the output used with solve from wolfram mathematica
# https://reference.wolfram.com/language/ref/Solve.html
