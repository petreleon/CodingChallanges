from parse import parse
from operator import methodcaller
import re
import numpy
import sys
from typing import Union

file_opened = open("input", 'r')
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
line = ''

print(dictOfValues)

def match(number: int, string :str, next_:list):
    global dictOfValues
    if isinstance(dictOfValues[number], str):
        if dictOfValues[number] == string[0]:
            if len(next_) == 0 and len(string) == 1:
                raise Exception()
            if len(next_) > 0 and len(string) > 1:
                match(next_[0], string[1:], next_[1:])
    if isinstance(dictOfValues[number], list):
        for list_ in dictOfValues[number]:
            match(list_[0], string, list_[1:] + next_)
        
matches = 0
[zero] = dictOfValues[0]
for index, line in enumerate(lines[lastLineIndex+1:]):
    try:
        for iterator in line:
            match(zero[0], line, zero[1:])
    except Exception:
        matches += 1
        print(line)
print(matches)
