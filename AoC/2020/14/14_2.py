from parse import parse
from operator import methodcaller
file_opened = open("input", 'r')
lines = file_opened.read().splitlines()
# lines.append('')
dictOfValues = dict()
mask = ""

def recursiveAdder(string, list_):
    if 'X' in string:
        index = string.find('X')
        recursiveAdder(string[:index]+'0'+string[index+1:], list_)
        recursiveAdder(string[:index]+'1'+string[index+1:], list_)
    else:
        list_.append(string)
# max_X_occurences = 0
# print( '{0:036b}'.format(101))
for index, line in enumerate(lines):
    # if line == '':
    #     pass
    word, value = parse("{} = {}", line)
    if word == 'mask':
        mask = value
        # X_occurences = value.count('X')
        # if X_occurences > max_X_occurences:
        #     max_X_occurences = X_occurences
    else:
        memory =  parse("mem[{:d}]", word)[0]
        value_ = int(value)
        memory_bin = '{0:036b}'.format(memory)
        memory_filtered = ''.join([filter_ if filter_=='1' or filter_ =='X' else memory_bin[index_] for index_, filter_ in enumerate(mask)])
        list_ = []
        recursiveAdder(memory_filtered, list_)
        for element in list_:
            dictOfValues[element] = value_
        

print(sum(dictOfValues.values()))
        

# print(max_X_occurences)
