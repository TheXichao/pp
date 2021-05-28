import random

def task1():
  length = float(input('length: '))
  width = float(input('width: '))

  result = length * width

  if length == width:
    print(f'this square has the area of {result}')
  else:
    print('the area of this rectangle is', result)

def task2():
  print('''Menu
  1. Music 
  2. History
  3. Design and technology
  4. exit
  please enter your choice''')

  choices = {
    1 :'Music',
    2 :'History',
    3 :'Design and technology'
  }

  user_choice = int(input())
  if user_choice != 4:
    print(choices[user_choice])
  else:
    print('goodbye')

def task3():
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)

  print('you got',dice1, dice2)
  if dice1 == dice2:
    score = dice1 + dice2
    score *= 2

    print('you scored double! your score is', score)

  else:
    score = dice1 + dice2

    print('your score is',score)

def task4():
  value = int(input('how much have you paid for: '))
  if value >= 200:
    dValue = value * 0.9
  elif value > 100:
    dValue = value * 0.95
  else:
    pass

  print('you own', value,',after discount it is', dValue)

def task5():

  import time
  parkingTime = 60* 60 * int(input('how long do you want to park for: '))

  currentTime = time.time()
  formatedCurrentTime = time.ctime(currentTime)
  expireTime = currentTime + parkingTime
  formatedExpireTime = time.ctime(expireTime)

  print('the current time is:', formatedCurrentTime)
  print('the expirey time is:', formatedExpireTime)

  if parkingTime<= 2*3600:
    print('the fee is 3.50 pound')
  elif parkingTime <= 4 * 3600:
    print('the fee is 5 pound')
  elif parkingTime <= 12 * 3600:
    print('the fee is 10 pound')

