from parse import parse

file_opened = open("input_2.txt", 'r')
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
beingDone = set()
workers = []
workersMax = 2
time = 0

def computeTime(char):
    return ord(char) - ord('A') + 1

begin = True
while len(stack) or len(workers) or len(beingDone) or begin:
    begin = False
    stack = sorted(set(key for key in dependsOf  if len( dependsOf[key]) == 0).difference(alreadyDone).difference(beingDone) )
    for iterator in range(workersMax-len(workers)):
        if iterator < len(stack):
            key = stack[iterator]
            keyOrder += stack[iterator]
            workers.append((computeTime(key), key))
            beingDone.add(stack[iterator])
    timeBypassed = min((computeTime(iterated[1]) for iterated in workers))
    time += timeBypassed
    print(timeBypassed)
    workers = [(worker[0] - timeBypassed, worker[1]) for worker in workers]
    for worker in beingDone:
        if worker[0] == 0:
            for key_2 in dependsFor[worker[1]]:
                dependsOf[key_2].remove(worker[1])
            beingDone.remove(worker[1])
            alreadyDone.add(worker[1])
    workers = [ worker for worker in workers if worker[0] > 0 ]
    

# time += max((worker[0] for worker in workers))
print(time)
