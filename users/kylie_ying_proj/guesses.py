import random

def guess(x):
  random_number = random.randint(1,x)
  guess = 0
  while guess != random_number:
    guess = int(input(f"Guess a number between 1 and {x}: "))
    if guess < random_number:
      print(f"sorry {random_number} is too low")
      print(f"hint: {type(random_number)} {random_number}")
    elif guess > random_number:
      print(f"your guess of {guess} is too high")
  
  print(f"you got it! its {guess}")
      
    

# guess(10)

def computer_guess(min, max):
  num_to_guess = int(input(f"What number to guess? "))
  print(f"The computer will guess your number which is currently {num_to_guess}")
  guess = random.randint(min,max)
  while guess != num_to_guess:
    print(f"the computer guessed: {guess}")
    if guess < num_to_guess:
      guess = random.randint(min+1,max)
      print(f"computers guess of {guess} is to low")
    elif guess > num_to_guess:
      guess = random.randint(min,max-1)
      print(f"computers guess of {guess} is too high")
      
    # guess = random.randint(min,max)
      
    
  
  print(f"computer guessed it right! its {guess}")
  
computer_guess(0,12)