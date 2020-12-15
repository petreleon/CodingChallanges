from parse import parse
from operator import methodcaller
posDictionary = dict()
numbers = [16,1,0,18,12,14,19]
# numbers = [0,3,6]
for index in range(len(numbers) - 1):
    posDictionary[numbers[index]] = index + 1
for index in range(len(numbers), 2020):
    lastNumber = numbers[-1]
    if lastNumber not in posDictionary:
        numbers.append(0)
    if lastNumber in posDictionary:
        numbers.append(index - posDictionary[lastNumber])
    posDictionary[lastNumber] = index

print(numbers[-1])  
# not 866
