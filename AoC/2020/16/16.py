from parse import parse
from operator import methodcaller
import re
file_opened = open("input", 'r')
lines = file_opened.read().splitlines()
# lines.append('')
# print( '{0:036b}'.format(101))

dictOfDetails = dict() 
for index, line in enumerate(lines):
    if line == '':
        lastLineIndex = index
        break
    name, min1, max1, min2, max2 = parse ("{}: {:d}-{:d} or {:d}-{:d}", line)
    dictOfDetails[name] = [[min1, max1], [min2, max2]]

validSeats = dictOfDetails["seat"]

def validator(value, comparerValues):
    return comparerValues[0][0] <= value <= comparerValues[0][1] or \
        comparerValues[1][0] <= value <= comparerValues[1][1]

listOfPossibilities = []
for i in range(len(dictOfDetails.keys())):
    listOfPossibilities.append(list(dictOfDetails.keys()))

def refresh(listOfPossibilities):
    for index, possibilities in enumerate(listOfPossibilities):
        if len(possibilities) == 1:
            for otherline in listOfPossibilities[:index]:
                if listOfPossibilities[index][0] in otherline:
                    otherline.remove(listOfPossibilities[index][0])
            for otherline in listOfPossibilities[index + 1:]:
                if listOfPossibilities[index][0] in otherline:
                    otherline.remove(listOfPossibilities[index][0])

def filterByValue(value, index, listOfPossibilities, dictOfDetails):
    listOfPossibilities[index] = [list_element for list_element in listOfPossibilities[index] if validator(value, dictOfDetails[list_element])]
    refresh(listOfPossibilities)

myLineIndex = lastLineIndex + 2

lastLineIndex += 5
sum_ = 0
for index, line in enumerate(lines[lastLineIndex:], lastLineIndex):
    values = list(map(int, line.split(',')))
    valid_ = True
    for index_2,value in enumerate(values):
        valid = False
        for validator_assets in dictOfDetails.values():
            valid = valid or validator(value, validator_assets)
        if not valid:
            sum_ += value
            valid_ = False
    if valid_: 
        for index_2, value in enumerate(values):
            filterByValue(value, index_2, listOfPossibilities, dictOfDetails)

myLine = list(map(int, lines[myLineIndex].split(',')))

for index_2, value in enumerate(myLine):
    filterByValue(value, index_2, listOfPossibilities, dictOfDetails)

dictOfCollumns = dict()
for index, value in enumerate(listOfPossibilities):
    dictOfCollumns[listOfPossibilities[index][0]] = index

verifier = re.compile('^departure')
departures = [key for key in dictOfCollumns.keys() if verifier.match(key)]
product_ = 1
for departure in departures:
    product_ *= myLine[dictOfCollumns[departure]]
print(sum_)

print(product_)
assert product_ != 22879
