def task_one():
  proverb = 'a picture\'s worth a thousand words' 
  proverbImage = proverb.replace('a picture', 'an image')

  firstO = proverb.find('o')

  proverbUpper = proverb.upper()

  print(proverbUpper,firstO, len(proverb),sep='\n')

def task_two():
  radius = int(input('what is the radius? '))
  print(radius**2*22/7)

def task_three():
  num1 = float(input('num1 :'))
  num2 = float(input('num2 '))

  print(f"The sum of {num1} and {num2} is {num1 + num2} \n the product of these two is {num1 * num2}")
