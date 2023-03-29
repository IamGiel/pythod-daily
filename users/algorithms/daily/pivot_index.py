from typing import List

def pivot_index(nums:List[int]) -> int:
  total_sum = sum(nums)
  left_sum = 0
  for i in range(len(nums)):
    # basically keep the total sum of array
    # keep a running sum from left to right = left_sum
    # to track the total to the right, subtract nums[i]
    
    print(f"current right_sum {total_sum - left_sum - nums[i]}")
    
    if left_sum == total_sum - left_sum - nums[i]:
        return i
    left_sum += nums[i]
  return -1

test = [2, 1, 7, 3, 6, 5, 6, 2]
# print(pivot_index(test))

# First, calculate the sum of all the numbers in the array. Let's call this variable total_sum.
# Initialize a variable called left_sum to 0.
# Loop through the array, and for each index i:
# a. If left_sum is equal to total_sum minus left_sum minus nums[i], then return i (this means that the sum of all the numbers to the left of i is equal to the sum of all the numbers to the right of i).
# b. Otherwise, add nums[i] to left_sum.
# If no such index exists, return -1.

# [1, 7, 3, 6, 5, 6] = 28


# ===============================
# practice

def pivot_index(nums: List[int])-> int:
  
  arr_total = sum(nums)
  running_left_sum = 0
  running_right_sum = 0
  for i in range(len(nums)):
    print("==========")
    running_right_sum = arr_total - running_left_sum - nums[i]
    print(f"running right: {running_right_sum}")
    print(f"running left: {running_left_sum}")
    print(f"array total ({arr_total}) - running left({running_left_sum}) = {arr_total-running_left_sum}")
    print(f"{nums}")
    print(f"current i: {i}")
    print(f"nums[i]: {nums[i]}")
   
    
    if running_left_sum == (arr_total-running_left_sum-nums[i]):
      return i
    running_left_sum += nums[i]

  return -1
  
  print(f"running left: {running_left_sum}")
  
print(pivot_index(test))

  

