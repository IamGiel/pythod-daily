def productExceptSelf(nums:list)->list:
  '''
  return a list of all the prod of nums except nums[i]
  do it in O(n)
  example:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]
    0 allowed in the nums list
  '''
  
  zero_count = nums.count(0)
  if zero_count > 1:
    return [0] * len(nums)
  elif zero_count == 1:
    product = 1
    for num in nums:
      if num != 0:
        product *= num
    result = [0] * len(nums)
    print(f"result in zero count = 1: {result}")
    result[nums.index(0)] = product
    print(f"result if 0 is 1: {result}")
    return result
  else:
    product = 1
    for num in nums:
      product *= num
    return [product // num for num in nums]
          
      
      
      
  
print(productExceptSelf([-1,1,0,-3,3]))