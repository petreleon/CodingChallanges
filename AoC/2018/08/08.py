from parse import parse

file_opened = open("input", 'r')
line = file_opened.read().splitlines()[0]
line = tuple(map( int, line.split(' ') ))
extractor_iterator = 0
def extractor():
    global extractor_iterator
    element = line[extractor_iterator]
    extractor_iterator += 1
    return element

sum_ = 0
def problem1():
    global sum_
    nodes = extractor()
    metadatas = extractor()
    for _ in range(nodes):
        problem1()
    for _ in range(metadatas):
        sum_+= extractor()
problem1()

print(sum_)

extractor_iterator = 0
def problem2():
    local_sum = 0

    nodesCount = extractor()
    metadatasCount = extractor()
    nodes = []
    metadatas = []
    for _ in range(nodesCount):
        nodes.append(problem2())
    for _ in range(metadatasCount):
        metadatas.append(extractor())
    if nodesCount == 0:
        local_sum = sum(metadatas)
        return local_sum
    
    local_sum = sum([nodes[metadata - 1]\
        for metadata in metadatas \
            if metadata <= len(nodes)])
    return local_sum

print(problem2())



