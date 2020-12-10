from parse import parse
from operator import methodcaller
file_opened = open("input", 'r')
lines = file_opened.read().splitlines()
# lines.append('')
listOfInts = []
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

print(list_[0]*list_[-1])
print(list_)

# def condition(a, b):
#     return a <= b


# sum_ = 3
# step = 1
# initStep = 0
# stopStep = len(listOfInts)
# stackList = [initStep]


# while stackList:
#     while stackList and not condition(stackList[-1], stopStep):
#         stackList.pop()
#         if stackList:
#             stackList[-1] += step
#     sum_ = sum( stackList)
#     # verify current solution
#     if sum_ == highRate:
#         print(stackList)
#     # can add to stack
#     elif stackList and len(stackList) < 4 and sum_ < highRate and condition(stackList[-1], stopStep):
#         stackList.append(stackList[-1] + 1 - step)
#     if len(stackList):
#         stackList[-1] += step

# print(listOfInts[0])