from parse import parse
from operator import methodcaller
import regex
import numpy
import sys
from typing import Union

file_opened = open("input3_", 'r')
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
    else:
        value = [[int(and_) for and_ in or_.split(' ')] for or_ in value.split(' | ')]
    dictOfValues[key] = value

def sum_(first:Union[str, list], second:Union[str, list]):
    list_ = list()
    if isinstance(first, str):
        list_.append(first)
    if isinstance(first, list):
        list_.extend(first)
    if isinstance(second, str):
        list_.append(second)
    if isinstance(second, list):
        list_.extend(second)
    return list_

def Solver(number):
    value = dictOfValues[number]
    if isinstance(value, str):
        return value
    str_ = '('
    if len(value) >= 1:
        for valueIterated in value[0]:
            if number == valueIterated:
                str_ += '(?1)'
            else:
                str_solve = Solver(valueIterated)
                if '|' not in str_solve:
                    str_solve = str_solve.replace('(', '').replace(')', '')
                str_ += str_solve
    if len(value) == 2:
        str_+='|'
        for valueIterated in value[1]:
            if number == valueIterated:
                str_ += '(?1)'
            else:
                str_solve = Solver(valueIterated)
                if '|' not in str_solve:
                    str_solve = str_solve.replace('(', '').replace(')', '')
                str_ += str_solve
    str_ += ')'

    return str_
toSolve = Solver( 0 )
regex_string = ""+toSolve+""
list_ = []
print(regex_string)
matches = 0
for index, line in enumerate(lines[lastLineIndex+1:]):
    if regex.match(regex_string, line):
        matches += 1
        list_.append(line)
        print(line)
assert 'aaabbbbbbaaaabaababaabababbabaaabbababababaaa' in list_
print(matches)



