from collections import defaultdict
from typing import List
import string


def groupAnagrams(words: List[str]) -> List[List[str]]:
  group = {}
  for word in words:
    count = [0]*26 # total number of letters (lowercased only)
    for char in word:
      if char.lower() in string.ascii_lowercase:
        index = string.ascii_lowercase.index(char.lower())
        print(f"index: {index}")
        count[index] = "*"
        print(f"count: {count}")
    key = tuple(count)
    print(f"key: {key}")
    if key not in group:
      group[key] = []
    group[key].append(word)
    
  return group.values()
        

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))