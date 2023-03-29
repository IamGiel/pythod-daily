def isAnagram(s:str, t:str)->bool:
  obj_s = {}
  obj_t = {}
  
  for char in s:
    obj_s[char] = obj_s.get(char,0)+1
      
  for char in t:
    obj_t[char] = obj_t.get(char,0)+1
      
      
  return obj_s == obj_t
      
  
print(isAnagram("hello", "lehols"))