import random

def play():
  user_selection = input(f"\n=========\nTYPE R for Rock, P for Paper, S for scissors: \n=========\n")
  computer_selection = random.choice(['r','p','s'])
  
  winner = compare(computer_selection, user_selection)
  if winner != 'stop':
    if user_selection == computer_selection:
      print(f"its a tie!")
    if winner == 'computer':
      print(f'computer got you this time!')
    elif winner == 'user':
      print(f'you got the computer this time!')
    
    play()
  
  else:
    print(f"==============================================\nTHANKS FOR PLAYING!")
  
  
computer_score, user_score = 0, 0

def compare(computer, user):
  # r > s > p
  global computer_score, user_score
  
  if computer_score == 3 or user_score == 3:
    print(f'GAME ENDED! scores are:\n computer: {computer_score}\n player: {user_score}')
    return 'stop'
  if computer == 'r' and user == 's':
    print(f"computer win's the round with a {computer}")
    computer_score += 1
  if computer == 'r' and user == 'p':
    print(f"user win's the round against computers {computer}")
    user_score += 1
  if computer == 's' and user == 'p':
    print(f"computer win's the round with a {computer}")
    computer_score += 1
  if computer == 's' and user == 'r':
    print(f"user win's the round against computers {computer}")
    user_score += 1
  if computer == 'p' and user == 'r':
    print(f"computer win's the round with a {computer}")
    computer_score += 1
  if computer == 'p' and user == 's':
    print(f"user win's the round against computers {computer}")
    user_score += 1
    
  print(f'scores:\ncomputer: {computer_score}\nplayer: {user_score}')
  
play()