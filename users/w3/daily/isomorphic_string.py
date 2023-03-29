

def is_isomorphic(s:str, t:str)-> bool:
  # constraints
  # if len(s) != len(t):
  #   return False
  # if len(s) < 2 or len(s) > 50000:
  #   return False
  # if s.isascii() == False or t.isascii() == False:
  #   return False
  
  # return True
  
  if not (2 <= len(s) <= 50000 and len(s) == len(t) and all(c.isascii() for c in s+t)):
      return False
    
 
  my_dict = {}
  my_dict2 = {}
  
  for key, value in zip(s,t):
    if key in my_dict:
      # print(f"there is a key with {key} in the dictionary and the value is {my_dict[key]}")
      if my_dict[key] != value:
        # print(f"looks like wre gonna override an existing value for key {key}")
        return False
    my_dict[key] = value
      
  for key, value in zip(t,s):
    if key in my_dict2:
      # print(f"there is a key with {key} in the dictionary and the value is {my_dict2[key]}")
      if my_dict2[key] != value:
        # print(f"looks like wre gonna override an existing value for key {key}")
        return False
    my_dict2[key] = value
    
  print(my_dict)
  print(my_dict2)
  return True
  
test = "Hello World!"
test2 = "À È Ì Ò Ù Ỳ Ǹ Ẁ"

s = "badc"
t = "baba"

# print(f"expecting true {test} ==> {is_isomorphic(test, test)}")
# print(f"expecting false {test2} ==> {is_isomorphic(test2, test2)}")

print(f"test {s} and {t}: {is_isomorphic(s,t)}")
