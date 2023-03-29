from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
  lookup=defaultdict(list)
  for s in strs:
    count = [0]*26 # number of lowercased letters
    for i in range(len(s)):
      count[ord(s[i]) - ord("a")] += 1 # one hot encoding
      print(f"count: {count} for s: {s}")
    lookup[tuple(count)].append(s)
  return lookup.values()      
    

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))