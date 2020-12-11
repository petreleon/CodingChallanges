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
    dictOfLife2 = dictOfLife
    dictOfLife = dict()
    for index in dictOfLife2:
        (indexY, indexX) = index
        listOfAdjacents = []
        
        listOfAdjacents.append(dictOfLife2.get((indexY+1, indexX), '.'))
        listOfAdjacents.append(dictOfLife2.get((indexY-1, indexX), '.'))
        listOfAdjacents.append(dictOfLife2.get((indexY, indexX+1), '.'))
        listOfAdjacents.append(dictOfLife2.get((indexY, indexX-1), '.'))
        listOfAdjacents.append(dictOfLife2.get((indexY+1, indexX+1), '.'))
        listOfAdjacents.append(dictOfLife2.get((indexY-1, indexX-1), '.'))
        listOfAdjacents.append(dictOfLife2.get((indexY-1, indexX+1), '.'))
        listOfAdjacents.append(dictOfLife2.get((indexY+1, indexX-1), '.'))
        occupied = listOfAdjacents.count('#')
        if dictOfLife2[index] == 'L' and occupied == 0:
            dictOfLife[index] = '#'
        elif dictOfLife2[index] == '#' and occupied >= 4:
            dictOfLife[index] = 'L'
        else:
            dictOfLife[index] = dictOfLife2[index]
    
print( list( dictOfLife.values()).count('#') )
        