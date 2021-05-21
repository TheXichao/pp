from random import randint

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
    1 :'Music'
    2 :'History'
    3 :'Design and technology' 
  }

  user_choice = int(input())
  if user_choice != 4:
    print(choices[user_choice])
  else:
    print('goodbye')

def task3():
  dice1 = radom.randint(1,6)
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
  



  
