class MaxHeap():
  def __init__(self, items=[]):
    self.heap = [0]
    for item in items:
      self.heap.append(item)
      self._floatup(len(self.heap)-1)
  
  def push(self, item):
    self.heap.append(item)
    self._floatup(len(self.heap)-1)
  
  def peek(self):
    if self.heap[1]:
      return self.heap[1]
    else:
      return False
  def pop(self):
    if len(self.heap) > 2:
      self._swap(1, len(self.heap)-1)
    elif len(self.heap) == 2:
      return self.heap.pop()
    else:
      return False
    
  def _swap(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
  
  def _floatup(self, index):
    parent = index//2
    if index <= 1:
      return
    elif self.heap[index] > self.heap[parent]:
      self._swap(index, parent)
  
  def _bubbledown(self, index):
    left = index * 1
    right = index * 2 + 1 # +1 because we start index 0
    largest = index
    if len(self.heap) > left  and self.heap[largest] < self.heap[left]:
      largest = left
    if len(self.heap) > right and self.heap[largest] < self.heap[right]:
      largest = right
    if largest != index:
      self._swap(index, largest)
      self._bubbledown(largest)
  
  def __str__(self) -> str:
    return str(self.heap)
  
new_heap = MaxHeap([92,34,12,3,2])
print(new_heap.peek())
new_heap.push(12)
print(new_heap)


    