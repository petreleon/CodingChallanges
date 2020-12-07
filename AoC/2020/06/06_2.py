from parse import parse
file_opened = open("input", 'r')
lines = file_opened.read().splitlines()
lines.append('')
answers = set()
answers_ = set()
sum_ = 0
first = True
for line in lines:
    if len( line ) == 0:
        first = True
        sum_ += len(answers)
        answers = set()
    if len( line ) != 0:
        for answer in line:
            answers_.add(answer)
        if first:
            answers = answers_
        answers = answers.intersection(answers_)
        answers_ = set()
        first = False

print(sum_)
