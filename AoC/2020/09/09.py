from parse import parse
from operator import methodcaller
file_opened = open("input", 'r')
lines = file_opened.read().splitlines()
# lines.append('')
listOfInts = list()
found = False
current_line = 0
while current_line < len(lines):
    line = lines[current_line]
    listOfInts.append(int(line))
    # if line == '':
    #     pass
    if current_line >= 25:
        valid = False
        for index1, value1 in enumerate(listOfInts[-26:-1]):
            for index2, value2 in enumerate(listOfInts[-26:-1]):
                if index1 != index2 and value1 + value2 == listOfInts[-1]:
                    valid = True
        if valid == False and not found:
            num = listOfInts[-1]
            found = True
    current_line += 1

found = False
for index1, value1 in enumerate(listOfInts):
    for index2, value2 in enumerate(listOfInts[index1+1:], start= index1+1):
        sum_ = sum(listOfInts[index1:index2+1])
        if sum_ == num:
            print(min(listOfInts[index1:index2+1]) + max(listOfInts[index1:index2+1]))
            found = True
            break
        if sum_ > num:
            break
    if found:
        break


