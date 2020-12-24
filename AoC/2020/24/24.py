from parse import parse
from operator import methodcaller
import operator
import re
import numpy
import sys
from typing import Union
import math
from collections import defaultdict

file_opened = open("input", 'r')
lines = file_opened.read().splitlines()
# lines = """sesenwnenenewseeswwswswwnenewsewsw
# neeenesenwnwwswnenewnwwsewnenwseswesw
# seswneswswsenwwnwse
# nwnwneseeswswnenewneswwnewseswneseene
# swweswneswnenwsewnwneneseenw
# eesenwseswswnenwswnwnwsewwnwsene
# sewnenenenesenwsewnenwwwse
# wenwwweseeeweswwwnwwe
# wsweesenenewnwwnwsenewsenwwsesesenwne
# neeswseenwwswnwswswnw
# nenwswwsewswnenenewsenwsenwnesesenew
# enewnwewneswsewnwswenweswnenwsenwsw
# sweneswneswneneenwnewenewwneswswnese
# swwesenesewenwneswnwwneseswwne
# enesenwswwswneneswsenwnewswseenwsese
# wnwnesenesenenwwnenwsewesewsesesew
# nenewswnwewswnenesenwnesewesw
# eneswnwswnwsenenwnwnwwseeswneewsenese
# neswnwewnwnwseenwseesewsenwsweewe
# wseweeenwnesenwwwswnew""".splitlines()
dictOfValues = dict()
neighbours = [(-2,0),(2,0),(1,1),(1,-1),(-1,1),(-1,-1)]
def neighboursGenerator(location:(int,int)):
    actualX, actualY = location
    return [(actualX + differenceX, actualY + differenceY) for (differenceX, differenceY) in neighbours]
for line in lines:
    x, y = 0,0
    while line:

        if re.match("^e", line):
            line = line[1:]
            x += 2
        if re.match("^w", line):
            line = line[1:]
            x -= 2
        if re.match("^ne", line):
            line = line[2:]
            x += 1
            y += 1
        if re.match("^nw", line):
            line = line[2:]
            x -= 1
            y += 1
        if re.match("^se", line):
            line = line[2:]
            x += 1
            y -= 1
        if re.match("^sw", line):
            line = line[2:]
            x -= 1
            y -= 1
    location = (x, y)
    dictOfValues[location] = not dictOfValues.get(location,False)

BLACK = True
WHITE = False

def isBlack(location:(int, int), dict_:dict):
    return dict_.get(location, WHITE)

def counter(dict_ :dict):
    count_ = 0
    for value in dict_.values():
        if value:
            count_+=1
    return count_

def blackTiles(location:(int, int), dict_ :dict):
    count_ = 0
    for locationIterator in neighboursGenerator(location):
        if isBlack(locationIterator, dict_):
            count_+=1
    return count_

def itShouldBe(location:(int, int), dict_ :dict):
    hexagon = isBlack(location, dict_)
    count_neighbours = blackTiles(location, dict_)
    if hexagon == BLACK and (count_neighbours == 0 or count_neighbours > 2):
        return WHITE
    if hexagon == WHITE and count_neighbours == 2:
        return BLACK
    return hexagon
print(counter(dictOfValues))
dictionary1 = dictOfValues
dictionary2 = dict()
for _ in range(100):
    dictionary2.clear()
    for location in dictionary1.keys():
        if itShouldBe(location, dictionary1):
            dictionary2[location] = BLACK
        # if isBlack(location, dictionary1):
        for location_neighbour in neighboursGenerator(location):
            if location_neighbour not in dictionary2.keys():
                if itShouldBe(location_neighbour, dictionary1):
                    dictionary2[location_neighbour] = BLACK
    print(counter(dictionary2))
    dictionary1,dictionary2 = dictionary2, dictionary1


