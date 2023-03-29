
from typing import List

test = ["cat", "bat", "woW", "OWL"]

# *at -> true, wo* -> true, *o* -> true

def words_in_dict(wordsList:List[str], test_word:str)->bool:
  '''
    will check if a word is in the wordsList
    handled added case: * in a word as wild card (any char)
  '''
  
  # iterate through the list
  # check if a word is in the list 
  # list comprehension to lowercase all strings
  
  # added task
  # asterisk in a word can be wild card or any letter
  # eg *at = true
  # eg *ut = false
  # eg wo* = true
  # eg wi = false
  # eg b*t = true
  # eg v*n = false
  
  # approach
  # check if there is an astersik
    # if theres one, find the index
    # convert all strings 
    # example test word = *at
    # remove asterisk = at
    # in the list, only compare to the letters in index 1 and 2
    
  
  
  wordsList = [word.lower() for word in wordsList] # O(n)
  have_asterisk = test_word.find('*')
  if have_asterisk != -1: # have an asterisk
    at_index = test_word.index('*')
    test_word = test_word.replace('*', '')
    wordsList = [w[:at_index]+w[at_index+1] for w in wordsList] # O(n)
    if test_word in wordsList:  
      return True
  else:
    if test_word in wordsList:
      return True
    
    
  return False

# print(f"testone: {words_in_dict(test, 'bat')}") # true
# print(f"testone: {words_in_dict(test, 'owl')}") # false
print(f"testone: {words_in_dict(test, 'b*p')}") # false
    