import random
from data.words import words
import string

# print(words)

def get_valid_word():
  chosen_word = random.choice(words)
  # dont get word with space or dash
  while "-" in chosen_word or " " in chosen_word:
    chosen_word = random.choice(words)
    
  # print(f"chosen word: {chosen_word.upper()}")
  return chosen_word.upper()
  
def hangman(tries:int):
  word = get_valid_word()
  word_letters = set(word) # letters in the word
  alphabet = set(string.ascii_uppercase)
  used_letter = set()
  max_attempts = tries
  correct_guesses = set()
  print("##############################################")
  print("=========== WELOCME TO HANGMAN =============")
  print(f"=========== GUESS THE WORD! YOU HAVE {max_attempts} ATTEMPTS =============")
  print(f"=========== This word has: {len(word_letters)} letters =============")
  print("##############################################")
  while int(len(word_letters)) > 0:
    if max_attempts == 0:
      print(f"NO more guesses left, try gain next time! The word to guess was: {word}")
      ask_to_play_again()
    
    word_list = [letter if letter in used_letter  else '-' for letter in word]
    print(f"??????????\nMYSTERY WORD: {' '.join(word_list)}\n???????????")
    user_letter = input("=============\nenter a letter: ").upper()
    if user_letter in alphabet - used_letter:
      used_letter.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
        correct_guesses.add(user_letter)
      else:
        max_attempts = max_attempts-1
        print(f"OOPS!!! invalid, '{user_letter}' is not in the guess word. You have {max_attempts} guesses left!")
    elif user_letter in used_letter:
      print(f"OOPS!!! invalid, you already picked '{user_letter}' before!")
    
    
  print(f"used letters: {used_letter}")
  print(f"your guessed it in {10 - max_attempts} attempts!, the word is '{word}'")
  ask_to_play_again()
  
def ask_to_play_again():
  play_again = input("Play again? \nType 'y' for yes or anything to exit")
  if play_again == 'y':
    hangman(10)
  else: 
    return None
  
    
    
  

  
hangman(10)
  