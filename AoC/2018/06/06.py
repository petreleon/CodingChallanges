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

for iterator_x in range(0, 500):
    for iterator_y in range(0, 500):
        current_manhattan = 1000
        double = False
        for iterator_point in points:
            iterator_manhattan = manhattan((iterator_x, iterator_y), iterator_point)
            if iterator_manhattan < current_manhattan:
                double = False
                current_Point = iterator_point
                current_manhattan = iterator_manhattan
            elif iterator_manhattan == current_manhattan:
                double = True
        if not double:
            pointsDictionary[current_Point] = pointsDictionary.get(current_Point,0) + 1
            if iterator_x == min_x or iterator_x == max_x or iterator_y == min_y or iterator_y == max_y:
                excludedPointSet.add(current_Point)

for excludedPoint in excludedPointSet:
    del pointsDictionary[excludedPoint]
print(max(pointsDictionary.values()))
