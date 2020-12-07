from parse import parse
from operator import methodcaller
import random
file_opened = open("input.txt", 'r')
lines = file_opened.read().splitlines()


def manhattan(point_A, point_B):
    return abs(point_A[0] - point_B[0]) + abs(point_A[1] - point_B[1])

points = set()
def makeComparing(pointOrigin):
    def compare(pointRemote):
        return manhattan(pointOrigin, pointRemote)
    return compare

for line in lines:
    point = tuple(map(int,line.split(', ')))
    points.add(point)
point = random.choice(tuple(points))
min_x = max_x = point[0]
min_y = max_y = point[1]
for point in points:
    if point[0] > max_x:
        max_x = point[0]
    if point[0] < min_x:
        min_x = point[0]
    if point[1] > max_y:
        max_y = point[1]
    if point[1] < min_y:
        min_y = point[1]
    
pointsFunctions = [(makeComparing(point), point) for point in points]
pointsDictionary = dict()
excludedPointSet = set()
region = 0
for iterator_x in range(0, 500):
    for iterator_y in range(0, 500):
        current_sum = 0
        for iterator_point in points:
            current_sum += manhattan((iterator_x, iterator_y), iterator_point)
        if current_sum < 10000:
            region += 1

print(region)
