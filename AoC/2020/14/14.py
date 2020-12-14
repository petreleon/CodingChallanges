from parse import parse
from operator import methodcaller
file_opened = open("input", 'r')
lines = file_opened.read().splitlines()
# lines.append('')
dictOfValues = dict()
mask = ""
# print( '{0:036b}'.format(101))
for index, line in enumerate(lines):
    # if line == '':
    #     pass
    word, value = parse("{} = {}", line)
    if word == 'mask':
        mask = value
    else:
        memory =  parse("mem[{:d}]", word)[0]
        value_ = '{0:036b}'.format(int(value))
        valueToStore = ''.join([value_[index_] if mask_ == 'X' else mask_ for index_, mask_ in enumerate(mask) ])
        dictOfValues[memory] = int(valueToStore, 2)

print(sum(dictOfValues.values()))