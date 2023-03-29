def isAnagram(s:str, t:str)->bool:
  obj_s = {}
  obj_t = {}
  
  for i in range(len(s)):
    if s[i] in obj_s:
      obj_s[s[i]] += 1
    else:
      obj_s[s[i]] = 1
  print(obj_s)
  
  for i in range(len(t)):
    if t[i] in obj_t:
      obj_t[t[i]] += 1
    else:
      obj_t[t[i]] = 1
 
  if obj_s == obj_t:
    return True
  
  return False
  
print(isAnagram("hello", "lehols"))