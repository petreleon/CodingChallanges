file_opened = open("input.txt", 'r')
lines = file_opened.readlines()
from parse import *
right_step = 3
down_step = 1
y = 0
x = 0
trees = 0

while y < len(lines):
    if lines[y][x] == '#':
        trees += 1
    y += down_step
    x += right_step
    x = x %  (len(lines[0]) - 1)
print(trees)
