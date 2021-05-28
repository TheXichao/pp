def task1():
    import random
    totalNum = int()
    for _ in range(10):
        num = random.randint(1,10)
        print('you got the number: ', num)
        totalNum += num
    print('total of the number: ',totalNum)

def task2():
    import random
    totalNum = int()
    for _ in range(1000):
        num = random.randint(1,10)
        totalNum += num
    print('the average is: ',totalNum/1000)


def task3():
    productCode = input('enter your product code, it should begin with AB or AS followed by 3 number: ')
