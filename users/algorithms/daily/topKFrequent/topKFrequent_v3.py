from collections import defaultdict, Counter
import heapq

def topKFrequent(nums:list, k:int)->list:
  '''
  Given any array of numbers, and k (a number), from the list
  return top K frequent elements
  
  can K be 0?
  can we have empty array 
  
  Input: nums = [1,1,1,2,2,3], k = 2
  Output: [1,2]
  
  '''
  # using heap module
  obj = {}
  heap = []
  most_freq = []
  for num in nums:
    # {
    #   3:1,
    #   0:2,
    #   1:1
    # }
    if num in obj:
      obj[num] += 1
    else:
      obj[num]=1
      
  # store it in heap, purpose is to get the max
  for el, freq in obj.items():
    print(f"element:{el}, frequency:{freq}")
    tupled = (-freq,el)
    heap.append(tupled)
    print(f"tupled:{tupled}")
    
  print(f"heap:{heap}")
  heapq.heapify(heap)
  print(f"heap heapified:{heap}")
  
  for i in range(k):
    freq, element = heapq.heappop(heap)
    print(f"freq:{freq}, element:{element}")
    most_freq.append(element)
  

  
      
  return tuple(most_freq)


    
    
  
  
print(topKFrequent(['a','b','b','c','c','c' ], 2))
  