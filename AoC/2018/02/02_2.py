from parse import parse
from operator import methodcaller
file_opened = open("input.txt", 'r')
lines = file_opened.read().splitlines()

commons = ""

for index_line, line in enumerate(lines):
    for second_line in lines[index_line+1:]:
        charDiff = 0
        lastDiff = -1
        for index_char, char in enumerate(line):
            if char != second_line[index_char]:
                lastDiff = index_char
                charDiff += 1
        if charDiff == 1:
            commons = line[:lastDiff] + line[lastDiff+1:]
            break
    if charDiff == 1:
        break

print(commons)

