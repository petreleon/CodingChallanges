from parse import parse
from operator import methodcaller
file_opened = open("input", 'r')
lines = file_opened.read().splitlines()
# lines.append('')
dictOfLife = dict()
for indexY, line in enumerate(lines):
    # if line == '':
    #     pass
    for indexX, char in enumerate(line):
        dictOfLife[(indexY, indexX)] = char

dictOfLife2 = dict()
maxY, maxX = max(dictOfLife.keys())
minY, minX = min(dictOfLife.keys())
while dictOfLife2 != dictOfLife:
    for Y in range(minY, maxY+1):
        for X in range(minX,maxX+1):
            print(dictOfLife[(Y, X)], end='')
        print('')
    print('')
    dictOfLife2 = dictOfLife
    dictOfLife = dict()
    for index in dictOfLife2:
        (indexY, indexX) = index
        listOfAdjacents = []
        YX = ((+1, 0),(+1, +1),(+1, -1),(-1, 0),(-1, +1),(-1, -1),(0,+1),(0,-1))
        for Y, X in YX:
            for i in range(1,1000):
                if dictOfLife2.get((indexY+i*Y, indexX+i*X), 'L')!='.':
                    listOfAdjacents.append(dictOfLife2.get((indexY+i*Y, indexX+i*X), 'L'))
                    break
        occupied = listOfAdjacents.count('#')
        if dictOfLife2[index] == 'L' and occupied == 0:
            dictOfLife[index] = '#'
        elif dictOfLife2[index] == '#' and occupied >= 5:
            dictOfLife[index] = 'L'
        else:
            dictOfLife[index] = dictOfLife2[index]
        
    
print( list( dictOfLife.values()).count('#') )
        