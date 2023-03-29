def longest_substring_no_repeats(strings:str)->int:
  if not strings:
    return 0
  combinations = set()
  # lengths = []
  res = 0
  # sliding window (eg left and right pointer)
  left = 0
  for right in range(len(strings)):
    chars = strings[right]
    while chars in combinations: # meaning its a duplicate
      combinations.remove(strings[left])
      left += 1
    combinations.add(chars)
    # lengths.append(len(combinations))
    current_substring = strings[left:right+1]
    print(f"current substring: {current_substring} length: {len(current_substring)}")
    res = max(res, len(current_substring))
  # return max(lengths)
  return res
    
  
print(longest_substring_no_repeats("abcabcaad"))