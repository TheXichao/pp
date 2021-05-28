def task1():
    alist = []
    alist.append('apple')
    blist = list()
    for _ in range(20):
        blist.append(0)
    clist = alist + blist
    lastC = clist[-1]
    clist.pop()

def task2():
    names = []
    name = ''
    while name != 'End':
        name = input('enter the name: ')
        names.append(name)

    print(names)

def task3():
    name = input('enter your name: ')
    markList = []
    day = 0
    for _ in range(10):
        day =+ 1

        markList.append(int(input('enter your score for',day)))

    marks = {name:markList}
    sortedMarks = sorted(markList, reverse = True)
