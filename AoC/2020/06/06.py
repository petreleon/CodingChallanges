from parse import parse
file_opened = open("input", 'r')
lines = file_opened.read().splitlines()
lines.append('')
answers = set()
sum_ = 0
for line in lines:
    if len( line ) == 0:
        sum_ += len(answers)
        answers = set()
    for answer in line:
        answers.add(answer)

print(sum_)
