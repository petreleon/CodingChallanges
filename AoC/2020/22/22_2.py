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
# lines = """Player 1:
# 9
# 2
# 6
# 3
# 1

# Player 2:
# 5
# 8
# 4
# 7
# 10""".splitlines()
lines = """Player 1:
43
19

Player 2:
2
29
14""".splitlines()
list_ = []
for index, line in enumerate( lines ):
    if "Player" in line:
        list_.append([])
    elif line != '':
        list_[-1].append(int(line))
lastCompat = []
recursiveSeen = set()
def recursiveCombat(list_):
    seen = set()
    global recursiveSeen
    global lastCompat
    winner = 1
    losser = 0
    
    while len(list_[0])!=0 and len(list_[1])!= 0:
        theValue = (tuple(list_[0]), tuple(list_[1]))
        if theValue in seen or theValue in recursiveSeen:
            winner, losser = 0,1
            return (winner, losser), list_[winner]
        seen.add((tuple(list_[0]), tuple(list_[1])))
        if list_[winner][0] < len(list_[winner]) and list_[losser][0] < len(list_[losser]):
            recursiveSeen.add(theValue)
            (winner, losser), _ = recursiveCombat([list_[0][1:],list_[1][1:]])
            # values.discard(theValue)
        elif list_[winner][0] < list_[losser][0]:
            winner, losser = losser, winner
        list_[winner].append(list_[winner][0])
        del list_[winner][0]
        list_[winner].append(list_[losser][0])
        del list_[losser][0]
    lastCompat = list_[winner]
    return (winner, losser), list_[winner]

recursiveCombat(list_)
sum_ = 0

# winner = 0
# losser = 1
# while len(list_[0]) > 0 and len(list_[1]) > 0:
#     list_[winner].append(list_[winner][0])
#     del list_[winner][0]
#     list_[winner].append(list_[losser][0])
#     del list_[losser][0]
#     recursiveCombat(list_)

# while len(lastCompat[1]) > 0:
#     list_[winner].append(list_[winner][0])
#     del list_[winner][0]
#     list_[winner].append(list_[losser][0])
#     del list_[losser][0]
for counter, element in enumerate(reversed(lastCompat),1):
    sum_ += element * counter
# assert sum_ != 33182
# assert sum_ != 9601
print(list_)
print(sum_)
