from parse import parse
from operator import methodcaller
import re
import numpy
file_opened = open("input", 'r')
lines = file_opened.read().splitlines()
# lines = '''.#.
# ..#
# ###'''.splitlines()
# lines.append('')
# print( '{0:036b}'.format(101))

def findNeighboards(dictionary: dict, position: tuple):
    direction = (-1, 0, 1)
    neighboards = 0
    for z in direction:
        for y in direction:
            for x in direction:
                if not(z==0 and y==0 and x==0):
                    neighboard = dictionary.get((position[0]+z,position[1]+y,position[2]+x), '.')
                    if neighboard == '#':
                        neighboards += 1
    return neighboards


dict2 = dict()
maxDim = 0
for index, line in enumerate(lines):
    for index2, char in enumerate(line):
        dict2[(0,index, index2)] = char
        if maxDim < index2 + 1:
            maxDim = index2 + 1
            

cubes = 0
for index in range(1,1+6):
    dict1 = dict2
    dict2 = dict()
    cubes = 0
    for indexZ in range(-index, index+1):
        # print (indexZ, end= '\n\n')
        for indexY in range(-index - maxDim, index+1 + maxDim):
            for indexX in range(-index - maxDim, index+1 + maxDim):
                cube = dict1.get((indexZ,indexY,indexX), '.')
                countNeighboards = findNeighboards(dict1, (indexZ,indexY,indexX))
                if cube == '#':
                    if 2 <= countNeighboards <= 3:
                        dict2[(indexZ,indexY,indexX)] = '#'
                        cubes += 1
                    else:
                        dict2[(indexZ,indexY,indexX)] = '.'
                if cube == '.':
                    if countNeighboards == 3:
                        dict2[(indexZ,indexY,indexX)] = '#'
                        cubes += 1
                    else:
                        dict2[(indexZ,indexY,indexX)] = '.'
        # for indexY in range(-index - maxDim, index+1 + maxDim):
        #     for indexX in range(-index - maxDim, index+1 + maxDim):
        #         cube = dict2.get((indexZ,indexY,indexX), '.')
        #         print(cube, end='')
        #     print('')
        # print('')

print(cubes)