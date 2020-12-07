from parse import parse

file_opened = open("input.txt", 'r')
lines = file_opened.read().splitlines()
dependsOf = dict()
dependsFor = dict()
for line in lines:
    result = parse("Step {} must be finished before step {} can begin.", line)
    if result[0] not in dependsOf:
        dependsOf[result[0]] = set()
    if result[1] not in dependsOf:
        dependsOf[result[1]] = set()
    if result[0] not in dependsFor:
        dependsFor[result[0]] = set()
    if result[1] not in dependsFor:
        dependsFor[result[1]] = set()
    dependsOf[result[1]].add(result[0])
    dependsFor[result[0]].add(result[1])

keyOrder = ''

for key in dependsOf:
    print('{} depinde de {}'.format( key, dependsOf[key] ))

stack = sorted(set(key for key in dependsOf if len( dependsOf[key] ) == 0 ))
alreadyDone = set()
while len(stack):
    key = stack[0]
    keyOrder += stack[0]
    alreadyDone.add(stack[0])
    for key_2 in dependsFor[key]:
        dependsOf[key_2].remove(key)
    stack = sorted(set(key for key in dependsOf if len( dependsOf[key] ) == 0 ).difference(alreadyDone))
print(keyOrder)
