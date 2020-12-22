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
list_ = []
for index, line in enumerate( lines ):
    if "Player" in line:
        list_.append([])
    elif line != '':
        list_[-1].append(int(line))
winner = list_[0]
losser = list_[1]
while len(list_[0])!=0 and len(list_[1])!= 0:
    if winner[0] < losser[0]:
        winner, losser = losser, winner
    winner.append(winner[0])
    del winner[0]
    winner.append(losser[0])
    del losser[0]

sum_ = 0
for counter, element in enumerate(reversed(winner),1):
    sum_ += element * counter
assert sum_ != 33182
print(sum_)
