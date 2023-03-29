def find_dupes(nums)-> bool:
  hashset = set()
  
  for num in nums:
    print(num)
    
    if num in hashset:
      print(f'ops we have a dupes! and its {num}')
      return True
    else:
      hashset.add(num)
      print('no dupes')
      return False
      
    
    
  print(hashset)
  
  return True


test = [1,2,4,3,1]    
find_dupes(test)