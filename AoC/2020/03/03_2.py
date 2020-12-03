file_opened = open("input.txt", 'r')
lines = file_opened.readlines()
from parse import *
right_step = 3
down_step = 1
init_y = 0
init_x = 0
trees = 0
product = 1
a = [[1,1], [3,1], [5,1], [7,1], [1,2]]
for i in a:
    right_step = i[0]
    down_step = i[1]
    x = init_x
    y = init_y
    trees = 0
    while y < len(lines):
        if lines[y][x] == '#':
            trees += 1
        y += down_step
        x += right_step
        x = x %  (len(lines[0]) - 1)
    product *= trees
print(product)
