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
from collections import deque  
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
# lines = """Player 1:
# 43
# 19

# Player 2:
# 2
# 29
# 14""".splitlines()
list_ = []
for index, line in enumerate( lines ):
    if "Player" in line:
        list_.append([])
    elif line != '':
        list_[-1].append(int(line))
lastCompat = []
t = 0
def play_game(D1, D2, is_p2):
    SEEN = set()
    while D1 and D2:
        global t
        t += 1
        my_key = (tuple(D1),tuple(D2))
        if my_key in SEEN and is_p2:
            return True,D1
        SEEN.add(my_key)
        c1,c2 = D1.popleft(), D2.popleft()
        if len(D1)>=c1 and len(D2)>=c2 and is_p2:
            NEW_D1 = deque([D1[x] for x in range(c1)])
            NEW_D2 = deque([D2[x] for x in range(c2)])
            p1_wins,_ = play_game(NEW_D1, NEW_D2, is_p2)
        else:
            p1_wins = c1>c2

        if p1_wins:
            D1.append(c1)
            D1.append(c2)
        else:
            D2.append(c2)
            D2.append(c1)
    if D1:
        return True,D1
    else:
        return False,D2


FIRST = 0
SECOND = 1

def recursiveCombat(deque_1, deque_2, deep):
    deque_1, deque_2, seen = deque(deque_1), deque(deque_2), set()
    if deep > 0 and max(deque_1) > max(deque_2):
        return FIRST, deque_1
    
    while deque_1 and deque_2:
        hash = (tuple(deque_1),tuple(deque_2))
        first, second = deque_1.popleft(), deque_2.popleft()
        # print(deep, first, second, hash)
        if hash in seen:
            return FIRST, hash[FIRST]
        seen.add(hash)
        if first < len(hash[FIRST]) and second < len(hash[SECOND]):
            winner, _ = recursiveCombat(deque([deque_1[x] for x in range(first)]), deque([deque_2[x] for x in range(second)]), deep+1)
        else:
            if first > second:
                winner = FIRST
            if second > first:
                winner = SECOND
        if winner == FIRST:
            deque_1.append(first)
            deque_1.append(second)
        if winner == SECOND:
            deque_2.append(second)
            deque_2.append(first)
    if deque_1:
        return FIRST, deque_1
    return SECOND, deque_2
_, lastCompat = recursiveCombat(deque(list_[0]),deque(list_[1]), 0)
# _, lastCompat = recursiveCombat(list_[0], list_[1], 0)
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
print(lastCompat)
print(sum_)
