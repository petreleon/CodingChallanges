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
# number = '389125467'
number = '467528193'
# number = '167384529'
cups = [int(i) for i in number]
dictOfValues = dict()

for index in range(len(cups)-1):
    dictOfValues[cups[index]] = cups[index + 1] 

dictOfValues[cups[-1]] = max(cups) + 1
for index in range(len(cups)+1, 1000000):
    dictOfValues[index] = index + 1
dictOfValues[1000000] = cups[0]
currentCup = cups[0] 
for _ in range(10000000):
    next_1 = dictOfValues[currentCup]
    next_2 = dictOfValues[next_1]
    next_3 = dictOfValues[next_2]
    next_4 = dictOfValues[next_3]
    destination = getDestination(currentCup, [next_1, next_2, next_3])
    destination_next = dictOfValues[destination]
    dictOfValues[currentCup], dictOfValues[destination], dictOfValues[next_3] = \
        next_4, next_1, destination_next
    # print(destination)
    currentCup = dictOfValues[currentCup]

next_1 = dictOfValues[1]
next_2 = dictOfValues[next_1]
# currentCup = dictGetter(1, dictOfValues)
# while currentCup != 1:
#     print(currentCup, end='')
#     currentCup = dictGetter(currentCup, dictOfValues)
print(next_1, next_2)
assert next_1 * next_2 != 38592283275
# print(dictOfValues)
print(next_1 * next_2)
# print(dictOfValues)