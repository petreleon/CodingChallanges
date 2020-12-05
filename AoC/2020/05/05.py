file_opened = open("input", 'r')
lines = file_opened.read().splitlines()
from parse import *
maxId = 0
listSeats = []
for i in range(128):
    listSeats.append("________")
setOfIDs = set()

for line in lines:
    line = line.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1')
    ID = int(line, 2)
    collumn = ID % 8
    row = ID // 8
    listSeats[row] = listSeats[row][:collumn] + '#' + listSeats[row][collumn+1:]  
    if ID > maxId:
        maxId = ID
    #problem 2 begins
    setOfIDs.add(ID)

for iteratorID in range(0,1024):
    if iteratorID not in setOfIDs and iteratorID+1 in setOfIDs and iteratorID-1 in setOfIDs:
        print(iteratorID)
# problem 2 ends

print(maxId)
# visualising data for problem 2
for line in listSeats:
    print(line)

