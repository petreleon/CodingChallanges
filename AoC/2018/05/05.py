from parse import parse
from operator import methodcaller
file_opened = open("input.txt", 'r')
lines = file_opened.read().splitlines()

def reactorMatch(first,second):
    if first.upper() == second.upper() and first != second:
        return True
    return False
sum_ = 0
for line in lines:
    beforeReact = ''
    afterReact = line
    while afterReact != beforeReact:
        beforeReact = afterReact
        for reactorIndex, reactor in enumerate(beforeReact):
            if reactorIndex < len(beforeReact) - 1:
                if reactorMatch(reactor, beforeReact[reactorIndex+1]):
                    afterReact = beforeReact[:reactorIndex]+beforeReact[reactorIndex+2:]
                    break
    sum_ += len(afterReact)

print(sum_)            
