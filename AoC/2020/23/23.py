from parse import parse
from operator import methodcaller
import operator
import re
import numpy
import sys
from typing import Union
import math
from collections import defaultdict

# number = '389125467'
number = '467528193'
cups = [int(i) for i in number]
def cupExtractor(i):
    return [cups[j%len(cups)] for j in range(i, i+3)]
def cupCurrent(i):
    return cups[(i-1)%len(cups)]
def destination(current, pickedUp):
    while True:
        current -= 1
        if current < 1:
            current = 9
        if current not in pickedUp:
            return current

currentCupIndex = 1
for _ in range(100):
    print(cups)
    currentCup = cupCurrent(currentCupIndex)
    pickedUp = cupExtractor(currentCupIndex)
    cups = [element for element in cups if element not in pickedUp]
    destination_ = destination(currentCup, pickedUp)
    currentDestinationIndex = cups.index(destination_)+1
    cups[currentDestinationIndex:currentDestinationIndex] = pickedUp
    currentCupIndex = cups.index(currentCup) + 2
indexOf1 = cups.index(1) + 2
print("".join([str(cupCurrent(number)) for number in range(indexOf1, indexOf1+8)]))

