from parse import parse
from operator import methodcaller
file_opened = open("input", 'r')
lines = file_opened.read().splitlines()
# lines.append('')
time = int(lines[0])
buses = lines[1].split(',')
busIDs = []
for iterated in buses:
    if iterated != 'x':
        busIDs.append(int(iterated))
found = False
for iteratedTime in range(time, time+max(busIDs)+1):
    for iteratedID in busIDs:
        if iteratedTime % iteratedID == 0:
            found = True
            print(iteratedID *(iteratedTime - time))
            break
    if found:
        break
 