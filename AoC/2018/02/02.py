from parse import parse
from operator import methodcaller
file_opened = open("input.txt", 'r')
lines = file_opened.read().splitlines()
twos = 0
threes = 0
for line in lines:
    chars = dict()
    for char in line:
        chars[char] = chars.get(char, 0) + 1
    if 2 in chars.values():
        twos += 1
    if 3 in chars.values():
        threes += 1
print(twos * threes)
