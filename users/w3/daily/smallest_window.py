# Given an integer array, find the smallest window sorting which will make the entire array sorted in increasing order. The solution should return a pair consisting of the starting and ending index of the smallest window.

  # Input : [1, 2, 3, 7, 5, 6, 4, 8]
  # Output: (3, 6)
  # Explanation: The array can be sorted from index 3 to 6 to get sorted version.

  # Input : [1, 3, 2, 7, 5, 6, 4, 8]
  # Output: (1, 6)
  # Explanation: The array can be sorted from index 1 to 6 to get sorted version.

  # If the array is already sorted, the solution should return None.

  # Input : [1, 2, 3, 4, 5]
  # Output: None
  # Explanation: The array is already sorted.

unosrted_arr = [1, 9, 2, 3, 12, 7, 5, 6, 4, 8]

def smallest_window_sorting(A):
  max_seen, min_seen = -float('inf'), float('inf')
  left, right = None, None
  n = len(A)
  # traverse left to right, keep track of max so far
  for i in range(n):
    print(f"A[i] {A[i]} and max_seen: {max_seen}")
    max_seen = max(max_seen, A[i])
    print(f"max seen so far {max_seen}")
    if A[i] < max_seen:
      right = i
      print(f"right: {right}")
  
  print(f'reversed order')
  
  # traverse right to left, keep track of min so far
  # for i in range(1,len(A)+1):
  for i in range(n-1, -1, -1):
    print(A[-i])
    min_seen = min(min_seen, A[i])
    print(f"min seen {min_seen}")
    if A[-i] > min_seen:
      print(f"min seen {min_seen} on index {A.index(min_seen)}")
      min_seen = A[-i]   
      left = i
      print(f"left: {left}")
      
  print(left, right)
    
# smallest_window_sorting(unosrted_arr)


def redo_smallest_window(arr):
  left, right = None, None
  running_min, running_max = float('inf'), -float('inf')  
  n = len(arr)
  
  for i in range(n):
    running_max = max(running_max, arr[i])
    print(running_max)
    if arr[i] < running_max:
      print(f"arr[i] is less thn running_max {running_max}")
      print(f"tracking i: {i}")
      left = i
      
  for i in range(n-1, -1, -1):
    print(i)
    running_min = min(running_min, arr[i])
    print(f"running_min: {running_min} (vs: {arr[i]})")
    if arr[i] > running_min:
      print(f"this is current i {i}")
      right = i
  
  
  print(right, left)
  return right,left
      
redo_smallest_window([1, 2, 3, 4, 5])
