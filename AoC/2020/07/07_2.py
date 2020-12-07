from parse import parse
from operator import methodcaller
file_opened = open("input", 'r')
lines = file_opened.read().splitlines()
# lines.append('')
dictBags = dict()
for line in lines:
    typeBag, bags_ = line.split(' bags contain ')
    bags_ = bags_[:-1] 
    bags = bags_.split(', ')
    bags_2 = [(int( bag[0] ), ' '.join(bag[1:-1]) ) if bag[0] != 'no' else (0, '') for bag in map(methodcaller("split", " "), bags)]
    dictBags[typeBag] = set()
    for bag in bags_2:
        if bag[1]!= '':
            dictBags[typeBag].add((bag[0], bag[1]))

def contains(typeBag):
    sum_ = 1
    for bag in dictBags[typeBag]:
        sum_ += bag[0] * contains(bag[1])
    return sum_

print(contains('shiny gold')-1)


