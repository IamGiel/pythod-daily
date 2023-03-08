'''
Given an integer array, find the maximum sum among all its subarrays.

Input : [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The maximum sum subarray is [4, -1, 2, 1]

Input : [-7, -3, -2, -4]
Output: -2
Explanation: The maximum sum subarray is [-2]

Input : [-2, 2, -1, 2, 1, 6, -10, 6, 4, -8]
Output: 10
Explanation: The maximum sum subarray is [2, -1, 2, 1, 6] or [6, 4] or [2, -1, 2, 1, 6, -10, 6, 4]
'''

def findMaxSubarraySum_brute_force(arr):
  # Write your code here...
  # is wrapping around allowed ?
  # will there be null values?
  # is there max len for sub-array?
  
  # each element will iterate through the rest of the element
  n = len(arr)
  current_max = -float('inf')
  best_max = -float('inf')
  nums = []
  if len(arr) == 1:
    return arr[0]
  for i in range(n):
    for j in range(i,n+1):
      nums = arr[i:j+1]
      print(f"curr nums: {nums}")
      current_max = max(current_max, sum(arr[i:j+1]))
      print(f"nums: {arr[i:j]} and sum: {sum(arr[i:j+1])}")
      if best_max < current_max:
        best_max = current_max
        print(f"nums: {arr[i:j]}")
  print(f"best max {best_max}")
  return best_max

nums = [-4, -3, -2]
findMaxSubarraySum_brute_force(nums)   
