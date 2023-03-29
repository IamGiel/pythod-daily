def containsDuplicate(nums:int)->bool:
  seen = set()
  for num in nums:
    if num in seen:
      return True
    seen.add(num)
  return False

print(containsDuplicate([1,2,3,1])) # true
print(containsDuplicate([1,2,3])) # false