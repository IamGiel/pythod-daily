from collections import defaultdict

def topKFrequent(nums:list, k:int)->list:
  '''
  Given any array of numbers, and k (a number), from the list
  return top K frequent elements
  
  can K be 0?
  can we have empty array 
  
  Input: nums = [1,1,1,2,2,3], k = 2
  Output: [1,2]
  
  '''
  element = defaultdict()
  left_most = 0
  
  for i in range(len(nums)):
    if nums[i] not in element:
      element[nums[left_most]] = []
      
    element[nums[i]].append(nums[i])
    left_most+=1
    
  sorted_items = sorted(element.items(), key=lambda item: sum(item[1]), reverse=True)
  sorted_dict = dict(sorted_items)
  top_two_keys = list(sorted_dict.keys())[:2]
      
  return top_two_keys

print(topKFrequent([1,1,1,2,2,3], 2))
  