from parse import parse
from operator import methodcaller
import re
import numpy
import sys

def compute(string1:str):
    begin = (string1.count('*') + string1.count('+'))*'('
    return str(eval(begin+string1.replace('+', ') +').replace('*', ') *')))

def compute2(string1:str):
    return str(eval('('+string1.replace('*', ') * (') +')'))

file_opened = open("input", 'r')
lines = file_opened.read().splitlines()
# lines.append('')
# lines = ['1 + 2 * 3 + 4 * 5 + 6']
sum_ = 0
for index, line in enumerate(lines):

    while '(' in line:
        Open = line.rfind('(')
        Close = line.find(')', Open)
        line = line[:Open] + compute2(line[Open+1:Close]) + line[Close+1:]
    sum_ += int(compute2(line))

    # sum_ += eval(line)
print(sum_)
assert sum_ != 22048857051 
