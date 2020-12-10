
sum_ = 0
step = 1
initStep = 0
stopStep = 200

stackList = [initStep]
def condition(a, b):
    return a <= b



while stackList:
    while stackList and not condition(stackList[-1], stopStep):
        stackList.pop()
        if stackList:
            stackList[-1] += step
    sum_ = sum(stackList)
    # verify current solution
    if sum_ == 1024:
        print(stackList)
    # can add to stack
    elif stackList and len(stackList) < 4 and sum_ < 1024 and condition(stackList[-1], stopStep):
        stackList.append(initStep - step)
    if len(stackList):
        stackList[-1] += step

