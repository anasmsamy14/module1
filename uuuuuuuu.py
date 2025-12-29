import random
b=str(random.randint(1,10))
h= True
print('Welcome to the Number Guessing Game! Try to guess the number I am thinking of between 1 and 10. ')
while h:
      u=int(input("Guess a number between 1 and 10: "))
      if u==int(b):
        print("You guessed correctly!")
       
      else:
         print("You guessed incorrectly. try again!")