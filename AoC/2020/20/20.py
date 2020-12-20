from parse import parse
from operator import methodcaller
import re
import numpy
import sys
from typing import Union
import math
pattern = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.splitlines()

file_opened = open("input", 'r')
lines = file_opened.read().splitlines()
dictOfValues = dict()
def flipVertically(value):
    dictOfValues[value].reverse()
def flipHorzontally(value):
    for line in dictOfValues[value]:
        line.reverse()

def rotate(value):
    len_ = len(dictOfValues[value])
    tile = dictOfValues[value]
    for iterator in range(0, len_//2 + 1, 1):
        for iterator2 in range(len_ - iterator * 2 - 1):
            last = len_ - 1 - iterator
            tile[iterator][iterator+iterator2], tile[last- iterator2 ][iterator],  tile[last][last - iterator2],  tile[iterator + iterator2][last] = \
                tile[last- iterator2 ][iterator],  tile[last][last - iterator2],  tile[iterator + iterator2][last], tile[iterator][iterator+iterator2]

def printTile(value):
    for line in dictOfValues[value]:
        print(''.join(line))
    print()

def compareMarginsHorizontally(tile1, tile2):
    Tile1 = dictOfValues[tile1]
    Tile2 = dictOfValues[tile2]
    return Tile1[-1] == Tile2[0]


def compareMarginsVertically(tile1, tile2):
    Tile1 = dictOfValues[tile1]
    Tile2 = dictOfValues[tile2]
    return [row[-1] for row in Tile1] == [row[0] for row in Tile2]


for index, line in enumerate(lines):
    if line == '':
        continue
    elif "Tile" in line:
        Tile = parse("Tile {:d}:", line)[0]
        dictOfValues[Tile] = []
    else:
        dictOfValues[Tile].append([char for char in line])

dictOfMap = dict()

def compareTwoCoordinates(possibleNeighborCoordinate: tuple, targetCoordinate: tuple, possibleNeighbor: int, targetValue: int):
    if possibleNeighborCoordinate[0] == targetCoordinate[0]:
        if possibleNeighborCoordinate[1] < targetCoordinate[1]:
            return compareMarginsVertically(possibleNeighbor, targetValue)
        if possibleNeighborCoordinate[1] > targetCoordinate[1]:
            return compareMarginsVertically(targetValue, possibleNeighbor)
    if possibleNeighborCoordinate[1] == targetCoordinate[1]:
        if possibleNeighborCoordinate[0] < targetCoordinate[0]:
            return compareMarginsHorizontally(possibleNeighbor, targetValue)
        if possibleNeighborCoordinate[0] > targetCoordinate[0]:
            return compareMarginsHorizontally(targetValue, possibleNeighbor)

# dictOfMap[(0,0)] = list(dictOfValues.keys())[0]
listOfDifferences = [(0,1), (1, 0), (0, -1), (-1, 0)]
fitting = False
maxY = 0
minY = 0
maxX = 0
minX = 0

# while len(dictOfMap) != len(dictOfValues):
#     alreadyImproved = True
#     for Y in range(minY, maxY + 1):
#         for X in range(minX, maxX + 1):
#             if (Y, X) not in dictOfMap:
#                 alreadyImproved = False
#                 break
#         if not alreadyImproved:
#             break
#     for coordinate in dictOfMap.keys():
#         for difference in listOfDifferences:
#             targetCoordinate = (coordinate[0] + difference[0], coordinate[1] + difference[1]) 
#             if targetCoordinate not in dictOfMap and (minY <= targetCoordinate[0] <= maxY and minX <= targetCoordinate[1] <= maxX or alreadyImproved):
#                 possibileNegibors = [(targetCoordinate[0] + difference_[0], targetCoordinate[1] + difference_[1]) for difference_ in listOfDifferences]
#                 for tile in dictOfValues.keys():
#                     if tile not in dictOfMap.values():
#                         alreadyMoved = False
#                         fitting = True
#                         for possibileNegibor in possibileNegibors:
#                             if possibileNegibor in dictOfMap.keys():
#                                 if not alreadyMoved:
#                                     alreadyMoved = True
#                                     for iteratorRotation in range(4):
#                                         if compareTwoCoordinates(possibileNegibor, targetCoordinate, dictOfMap[possibileNegibor], tile):
#                                             break
#                                         flipHorzontally(tile)
#                                         if compareTwoCoordinates(possibileNegibor, targetCoordinate, dictOfMap[possibileNegibor], tile):
#                                             break
#                                         flipVertically(tile)
#                                         if compareTwoCoordinates(possibileNegibor, targetCoordinate, dictOfMap[possibileNegibor], tile):
#                                             break
#                                         flipHorzontally(tile)
#                                         if compareTwoCoordinates(possibileNegibor, targetCoordinate, dictOfMap[possibileNegibor], tile):
#                                             break
#                                         flipVertically(tile)
#                                         rotate(tile)
#                                     if not compareTwoCoordinates(possibileNegibor, targetCoordinate, dictOfMap[possibileNegibor], tile):
#                                         fitting = False
#                                         break
#                         if fitting:
#                             break
#             if fitting:
#                 break
#         if fitting:
#             break
#     if fitting:
#         fitting = False
#         dictOfMap[targetCoordinate] = tile
#         maxY = max(maxY, targetCoordinate[0])
#         minY = min(minY, targetCoordinate[0])
#         maxX = max(maxX, targetCoordinate[1])
#         minX = min(minX, targetCoordinate[1])

def isFitting(targetCoordinate, targetValue):
    fitting = True
    alreadyMoved = False
    for possibileNeigbor in [(targetCoordinate[0]+difference[0], targetCoordinate[1]+difference[1]) for difference in listOfDifferences]:
        if possibileNeigbor in dictOfMap:
            if alreadyMoved == False:
                alreadyMoved = True
                for _ in range(4):
                    if compareTwoCoordinates(possibileNeigbor, targetCoordinate, dictOfMap[possibileNeigbor], targetValue):
                        break
                    flipHorzontally(targetValue)
                    if compareTwoCoordinates(possibileNeigbor, targetCoordinate, dictOfMap[possibileNeigbor], targetValue):
                        break
                    flipVertically(targetValue)
                    if compareTwoCoordinates(possibileNeigbor, targetCoordinate, dictOfMap[possibileNeigbor], targetValue):
                        break
                    flipHorzontally(targetValue)
                    if compareTwoCoordinates(possibileNeigbor, targetCoordinate, dictOfMap[possibileNeigbor], targetValue):
                        break
                    flipVertically(targetValue)
                    rotate(targetValue)
                if not compareTwoCoordinates(possibileNeigbor, targetCoordinate, dictOfMap[possibileNeigbor], targetValue):
                    fitting = False
                    break
    return fitting

dimension = int( math.sqrt(len(dictOfValues)) )
def recursiveBacktrack(value: int, coordinate: tuple) -> None:
    global dictOfValues
    global dictOfMap
    global dimension
    if isFitting(coordinate, value):
        dictOfMap[coordinate] = value
        if len(dictOfMap) == len(dictOfValues):
            raise Exception()
        nextCoordinate = (coordinate[0]+(coordinate[1]+1)//dimension, (coordinate[1]+1)%dimension)
        for value in dictOfValues.keys():
            if value not in dictOfMap.values():
                recursiveBacktrack(value, nextCoordinate)
        del dictOfMap[coordinate]

listOfActions = [flipHorzontally, flipVertically, flipHorzontally, flipVertically]
gross = []

def rotate_():
    global value
    rotate(value)

try:
    for value in dictOfValues:
        for _ in range(4):
            dictOfMap = dict()
            rotate(value)
            recursiveBacktrack(value, (0,0))
except:
    value = dictOfMap[(0,0)]
    for Y in range(dimension):
        for X in range(dimension):
            print()
            print((Y,X))
            for Y_ in dictOfValues[ dictOfMap[(Y,X)] ]:
                for X_ in Y_:
                    print(X_, end='')
                print()
            
    print(dictOfMap[(0,0)]*dictOfMap[(0,dimension-1)]*dictOfMap[(dimension-1,0)]* dictOfMap[(dimension-1, dimension-1)])
    
    mapConstructed = []
    for Y in range(dimension):
        for X in range(dimension):
            # if X == 0:
            #     beginX = 0
            # else:
            #     beginX = 1
            # if Y == 0:
            #     beginY = 0
            # else:
            #     beginY = 1
            tileWithRemovedBorders = [line[1:len(line) - 1] for line in dictOfValues[ dictOfMap[(Y, X)] ][1:len(dictOfValues[ dictOfMap[(Y, X)]]) - 1]]
            if X == 0 and Y == 0:
                mapConstructed = tileWithRemovedBorders
            elif X == 0:
                mapConstructed.extend( tileWithRemovedBorders )
            else:
                for lineIterator in range(-len(tileWithRemovedBorders), 0):
                    mapConstructed[lineIterator].extend(tileWithRemovedBorders[lineIterator])
    # for Line in mapConstructed:
    #     for char in Line:
    #         print(char, end='')
    #     print()
    dictOfValues[value] = mapConstructed
    for _ in range(4):
        for action in listOfActions:
            foundMonsterAtMap = dict()
            
            for indexY in range(len(mapConstructed) - len(pattern)+1):
                for indexX in range(len(mapConstructed[0]) - len(pattern[0])+1):
                    foundAMonster = True
                    for indexMonsterY, rowMonster in enumerate(pattern):
                        for indexMonsterX, charMonster in enumerate(rowMonster):
                            if charMonster == '#' and mapConstructed[indexMonsterY+indexY][indexMonsterX+indexX]!= '#':
                                foundAMonster = False
                    if foundAMonster:
                        for indexMonsterY, rowMonster in enumerate(pattern):
                            for indexMonsterX, charMonster in enumerate(rowMonster):
                                if charMonster == '#':
                                    foundMonsterAtMap[(indexY+indexMonsterY,indexX+indexMonsterX)] = True

                if len(foundMonsterAtMap) > 0:
                    total = 0
                    for line in mapConstructed:
                        for char in line:
                            if char == '#':
                                total += 1
                    gross.append(total - len(foundMonsterAtMap))
            action(value)
        rotate(value)
    print(min(gross))
