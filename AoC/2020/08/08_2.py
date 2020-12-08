from parse import parse
from operator import methodcaller
file_opened = open("input", 'r')
lines = file_opened.read().splitlines()
# lines.append('')
lineToExecute = 0
beginned = False
operation = 0
alreadyExecutedLines = set()

lines_formatted = [list(parse('{} {:d}', line)) for line in lines]

for index in range(len(lines)):
    accumulator = 0
    isRepeated = False
    lineToExecute = 0
    alreadyExecutedLines = set()
    if lines_formatted[index][0] == 'jmp':
        lines_formatted[index][0] = 'nop'
        while lineToExecute < len(lines):
            if lineToExecute in alreadyExecutedLines:
                isRepeated = True
                break
            alreadyExecutedLines.add(lineToExecute)
            line = lines_formatted[lineToExecute]
            if line[0] == 'nop':
                lineToExecute += 1
            if line[0] == 'acc':
                accumulator += line[1]
                lineToExecute += 1
            if line[0] == 'jmp':
                lineToExecute += line[1]
        lines_formatted[index][0] = 'jmp'
    if lines_formatted[index][0] == 'nop':
        lines_formatted[index][0] = 'jmp'
        while lineToExecute < len(lines):
            if lineToExecute in alreadyExecutedLines:
                isRepeated = True
                break
            alreadyExecutedLines.add(lineToExecute)
            line = lines_formatted[lineToExecute]
            if line[0] == 'nop':
                lineToExecute += 1
            if line[0] == 'acc':
                accumulator += line[1]
                lineToExecute += 1
            if line[0] == 'jmp':
                lineToExecute += line[1]
        lines_formatted[index][0] = 'nop'
    if (lines_formatted[index][0] == 'jmp' or lines_formatted[index][0] == 'nop') and isRepeated == False:
        print(accumulator)
        break


