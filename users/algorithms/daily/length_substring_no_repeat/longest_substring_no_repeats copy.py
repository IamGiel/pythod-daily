def longest_substring_no_repeats(strings:str)->int:
  combinations = set()
  left = 0
  res = 0
  for i in range(len(strings)):
    chars = strings[i]
    print(f"char: {chars} combination: {combinations}")
    while chars in combinations:
     
      print(f"chars {strings[i]} are in combinations {combinations}")  
      combinations.remove(strings[left])
      print(f"after removing char {strings[i]} in combinations {combinations}")  
      left += 1
    combinations.add(chars)
    
    # check the current substring
    current_substring = strings[left:i+1]
    print(f"current_substring: {current_substring}")
    res = max(res, len(current_substring))
    
  print(combinations)
  return res
  
print(longest_substring_no_repeats("abcabcaad"))