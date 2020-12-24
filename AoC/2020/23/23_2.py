from parse import parse
from operator import methodcaller
import operator
import re
import numpy
import sys
from typing import Union
import math
from collections import defaultdict

def getDestination(current, list_):
    while True:
        current -= 1
        if current == 0:
            current = 1000000
        if current not in list_:
            return current
number = '389125467'
# number = '467528193'
cups = [int(i) for i in number]
dictOfValues = dict()
def dictGetter(value, dict_):
    return dict_.get(value,value%1000000 +1)
for index in range(len(cups),0,-1):
    if index < len(cups):
        dictOfValues[cups[index-1]] = cups[index]
    else:
        dictOfValues[cups[index-1]] = index+1

currentCup = cups[0] 
for _ in range(10000000):
    next_1 = dictGetter(currentCup, dictOfValues)
    next_2 = dictGetter(next_1, dictOfValues)
    next_3 = dictGetter(next_2, dictOfValues)
    next_4 = dictGetter(next_3, dictOfValues)
    destination = getDestination(currentCup, [next_1, next_2, next_3])
    destination_next = dictGetter(destination, dictOfValues)
    dictOfValues[currentCup], dictOfValues[destination], dictOfValues[next_3] = \
        next_4, next_1, destination_next
    currentCup = dictGetter(currentCup, dictOfValues)

next_1 = dictGetter(1, dictOfValues)
next_2 = dictGetter(next_1, dictOfValues)
print(next_1 * next_2)
