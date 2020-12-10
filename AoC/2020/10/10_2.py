from parse import parse
from operator import methodcaller
file_opened = open("input", 'r')
lines = file_opened.read().splitlines()
# lines.append('')
listOfInts = [0]
for index, line in enumerate(lines):
    # if line == '':
    #     pass
    listOfInts.append(int(line))

highRate = max(listOfInts) + 3
listOfInts.append(highRate)
listOfInts.sort()
list_ = [0, 0, 0]
step = 0
for integer in listOfInts:
    list_[integer - step -1] += 1
    step = integer



def condition(a, b):
    return a <= b

last_possibilities = 1
sum_ = 3
step = 1
initStep = 1
stopStep = 3
stackList = [initStep]
possibilities = 0
lastStackSum = 0
lastIntegerListIndex = 0
integerLists = []


for index, integer in enumerate(listOfInts):
    possibilities = 0
    if integer - 1 in listOfInts and index > 3:
        possibilities += 1
    if integer - 2 in listOfInts and index > 3:
        possibilities += 1
    if integer - 3 in listOfInts  and index > 3:
        possibilities += 1
    if possibilities == 1 and integer - 3 in listOfInts:
        integerLists.append(listOfInts[lastIntegerListIndex:index])
        lastIntegerListIndex = index

integerLists.append(listOfInts[lastIntegerListIndex:])

for integerList in integerLists:
    if len(integerList) >= 2:
        possibilities = 0
        stackList = [initStep]
        while stackList:
            while stackList and not condition(stackList[-1], stopStep):
                stackList.pop()
                if stackList:
                    stackList[-1] += step
            sum_ = sum( stackList ) + integerList[0] 
            # verify current solution
            if sum_ == integerList[-1]:
                # (stackList)
                possibilities += 1
            # can add to stack
            elif stackList and sum_ in integerList and condition(stackList[-1], stopStep):
                stackList.append(initStep - step)
            if len(stackList):
                stackList[-1] += step
    else:
        possibilities = 1

    last_possibilities *= possibilities

# assert last_possibilities > 1511207993344

print(last_possibilities)