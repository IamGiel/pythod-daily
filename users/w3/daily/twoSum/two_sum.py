
from typing import Tuple, List

def twoSum(nums:List[int], target:int)->Tuple[int,int]:
  '''
  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

  You may assume that each input would have exactly one solution, and you may not use the same element twice.

  You can return the answer in any order.
  '''
  
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      sum = nums[i]+nums[j]
      if sum == target:
        return i,j
      
print(f"two sum: {twoSum([1,2,2,3], 5)}")