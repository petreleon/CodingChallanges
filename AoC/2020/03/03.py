file_opened = open("input.txt", 'r')
lines = file_opened.readlines()
from parse import *
right_step = 3
down_step = 1
init_y = 0
init_x = 0
trees = 0

while init_y < len(lines):
    if lines[init_y][init_x] == '#':
        trees += 1
    init_y += down_step
    init_x += right_step
    init_x = init_x %  (len(lines[0]) - 1)
print(trees)
