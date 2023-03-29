from collections import defaultdict
from typing import List
import string


def groupAnagrams(words: List[str]) -> List[List[str]]:
  # create an dictionary, to avoid typerror use `defaultdict` from collections module
  # loop over the string `for word in words`
  # create var that will hold encoder = [0]*26
  # loop through each chars in the word: `for char in words`
  # then set encoder so that each chars index will map to encoders index
  # for example, character a is index 0 of encoder and result in [1,0,0 ... 0,0]
  
  combination = defaultdict(list)
  
  for word in words:
    encoder = [0]*26 # number of lowercased letters
    for char in word:
      # get the index of letter in ascii_lowercase
      index = string.ascii_lowercase.index(char.lower())
      encoder[index] += 1
      
    print(f"encoder:{encoder} for letter: {word}")
    combination[tuple(encoder)].append(word)
  print(combination.values())
        

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))