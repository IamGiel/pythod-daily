
from typing import Tuple, List

def twoSum(nums:List[int], target:int)->Tuple[int,int]:
  '''
  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

  You may assume that each input would have exactly one solution, and you may not use the same element twice.

  You can return the answer in any order.
  '''
  
  lookup = {}
  
  for i in range(len(nums)):
    complement = target - nums[i]
    print(f"complement: {complement}")
    if complement in lookup:
      print(f"lookup[complement]: {lookup[complement]}")
      return lookup[complement], i
    lookup[nums[i]] = i
    
      
print(f"two sum: {twoSum([1,2,2,3], 5)}")