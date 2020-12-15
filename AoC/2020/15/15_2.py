from parse import parse
from operator import methodcaller
posDictionary = dict()
numbers = [16,1,0,18,12,14,19]
# numbers = [0,3,6]
for index in range(len(numbers) - 1):
    posDictionary[numbers[index]] = index + 1
lastNumber = numbers[-1]
for index in range(len(numbers), 30000000):
    if lastNumber not in posDictionary:
        lastNumber_ = 0
    if lastNumber in posDictionary:
        lastNumber_ = index - posDictionary[lastNumber]
    posDictionary[lastNumber] = index
    lastNumber = lastNumber_

print(lastNumber)  
# not 866
