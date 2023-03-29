from collections import defaultdict

import heapq

def topKFrequent(nums, k):
  freq = {}
  for num in nums:
    freq[num] = freq.get(num, 0) + 1
  
  max_heap = []
  for num, count in freq.items():
    heapq.heappush(max_heap, (-count, num))
    if len(max_heap) > k:
      heapq.heappop(max_heap)
    print(f"this maxheap: {max_heap}")
  return [num for _, num in reversed(max_heap)]


print(topKFrequent([1,1,1,2,2,3], 2))
  