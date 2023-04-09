def productExceptSelf(nums:list)->list:
  '''
  return a list of all the prod of nums except nums[i]
  do it in O(n)
  example:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]
    
    0 is not handled here, assuming there are non ZERO entry
  '''
  
  result = [0] * len(nums) # [0,0,0,0]
  print(f"result:{result}")
  
  # var to store product in nums
  product = 1
      
  
  for i in range(len(nums)):
    product *= nums[i]
    print(f"prod:{product}")
  
  print(f"prod:{product}")
  
  for i in range(len(nums)):
    print(f"product:{product} // current i:{nums[i]}")
    result[i] = product // nums[i]
    
  print(f"result:{result}")
  
productExceptSelf([-1,1,0,-3,3])