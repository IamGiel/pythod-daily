from collections import defaultdict, Counter

def topKFrequent(nums:list, k:int)->list:
  '''
  Given any array of numbers, and k (a number), from the list
  return top K frequent elements
  
  can K be 0?
  can we have empty array 
  
  Input: nums = [1,1,1,2,2,3], k = 2
  Output: [1,2]
  
  '''
  # using heap module
  obj = {}
  
print(topKFrequent([3,0,1,0], 2))
  