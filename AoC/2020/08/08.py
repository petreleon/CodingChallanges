from parse import parse
from operator import methodcaller
file_opened = open("input", 'r')
lines = file_opened.read().splitlines()
# lines.append('')
lineToExecute = 0
beginned = False
operation = 0
alreadyExecutedLines = set()
lineThatCauseInfinityLoop = -2
lineThatCauseInfinityLoopConfirmed = -2

# while lineThatCauseInfinityLoopConfirmed != -1:
#     lineThatCauseInfinityLoopConfirmed = -1
#     while lineToExecute < len(lines):
#         if lineToExecute in alreadyExecutedLines:
#             lineThatCauseInfinityLoopConfirmed = lineThatCauseInfinityLoop
#             break
#         lineThatCauseInfinityLoop = lineToExecute
#         alreadyExecutedLines.add(lineToExecute)
#         line = lines[lineToExecute].split(' ')
#         line[1] = int(line[1])
#         if line[0] == 'nop':
#             lineToExecute += 1
#         if line[0] == 'acc':
#             operation += line[1]
#             lineToExecute += 1
#         if line[0] == 'jmp':
#             lineToExecute += line[1]
#     # lines[lineThatCauseInfinityLoop] = 'nop 0'
#     alreadyExecutedLines = set()
# print(operation)
# operation = 5
while lineToExecute < len(lines):
    if lineToExecute in alreadyExecutedLines:
        break
    alreadyExecutedLines.add(lineToExecute)
    line = lines[lineToExecute].split(' ')
    line[1] = int(line[1])
    if line[0] == 'nop':
        lineToExecute += 1
    if line[0] == 'acc':
        operation += line[1]
        lineToExecute += 1
    if line[0] == 'jmp':
        lineToExecute += line[1]

print(operation)
