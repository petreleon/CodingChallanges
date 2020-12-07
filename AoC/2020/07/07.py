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
            dictBags[typeBag].add(bag[1])

def containsShinyGold(typeBag):
    if "shiny gold" in dictBags[typeBag]:
        return True
    for bag in dictBags[typeBag]:
        if bag == (0, ''):
            return False
    if any([containsShinyGold(bags) for bags in dictBags[typeBag]]):
        return True
    return False

print(sum(map(containsShinyGold, dictBags.keys())))


