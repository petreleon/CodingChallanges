from parse import parse
from operator import methodcaller
import re
import numpy
import sys
from typing import Union

file_opened = open("input4", 'r')
lines = file_opened.read().splitlines()
lastLineIndex = 0

dictOfValues = dict()


# lines.append('')
for index, line in enumerate(lines):
    if line == '':
        lastLineIndex = index
        break
    (key, value) = parse("{:d}: {}", line)
    if "\"" in value:
        value = parse("\"{}\"", value)[0]
    if "|" in value:
        try:
            value1, value2 = parse("{} | {}", value)
            value = [list(map(int, value1.split(' '))), list(map(int, value2.split(' ')))]
        except:
            pass
    if "|" not in value and isinstance(value, str):
        try:
            value = [list(map(int,value.split(" ")))]
        except:
            pass
    dictOfValues[key] = value

begin = 0


def Solver(number):
    value = dictOfValues[number]
    if isinstance(value, str):
        return value
    str_ = '(('
    if len(value) >= 1:
        for valueIterated in value[0]:
            str_+=Solver(valueIterated)
    if len(value) == 2:
        str_+=')|('
        for valueIterated in value[1]:
            str_+=Solver(valueIterated)
    str_ += '))'
    return str_
toSolve = Solver( 0 )
regex = re.compile("^"+toSolve+"$")
solved = False
while not solved:
    solved = True
    
matches = 0
for index, line in enumerate(lines[lastLineIndex+1:]):
    if regex.match(line):
        matches += 1
print(matches)


    

