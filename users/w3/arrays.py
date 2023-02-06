#  Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21
import numpy as np

arr = np.arange(10,22,1).reshape(3,4)
arr

z = np.zeros((3,4))
z
type(z.shape)

z.size

# array([[10, 11, 12, 13],
#        [14, 15, 16, 17],
#        [18, 19, 20, 21]])

# Write a NumPy program to find the number of rows and columns of a given matrix.

def find_rows_cols_of_matrix(matrix:np.ndarray):
    return {
        "rows": matrix.shape[0],
        "cols": matrix.shape[1],
    }

find_rows_cols_of_matrix(arr)

# Write a NumPy program to create a 3x3 identity matrix, i.e. diagonal elements are 1, the rest are 0. Go to the editor
diag1 = np.identity((3), dtype=int)
diag1
diag1[0,0] = 4
# diag1[1,1] = 1
# diag1[2,2] = 1

diag1

x=np.where(diag1==0) 
x
for i in x:
    diag1[x]=np.random.randint(low=10,high=20)
    print(diag1[1])
    
randomarr = np.random.randint(0,10,(3,3)) 
randomarr

multiplier = 10
x = np.where(randomarr != 9, multiplier, multiplier*10)
x

row = 10
for i in range(0,row+1):
  for j in range(0, i + 1):
    print(f"✅", end=" ")
  if i == 1:
    print(f"{i}st row")
  elif i == 2:
    print(f"{i}nd row")
  elif i == 3:
    print(f"{i}rd row")
  else:
    print(f"{i}th row")


fruits = ["apple", "banana", "grapes"]
num_items = ["three", "two", "one"]
for i in fruits:
  for j in num_items:
    print(i,j)
  print('-- gap --')
  
numToadd = [10,20,30]
nums = [1,2,3]

for i in numToadd:
  for j in nums:
    print(f"{i} add {j} = {i+j}")

#  square
row = 10
for i in range(0,row+1):
  for j in range(0, row+1):
    print("*", end=" ")
  print(" ")

#  sliding right triangle
row = 10
for i in range(0,row+1): 
  for j in range(0, i+1):
    print("*", end=" ")
  print(" ")
  
#  upside down right triangle
row = 10
for i in range(0,row+1): 
  for j in range(i, 11):
    print("*", end=" ")
  print(" ")
  
fruits = ["apple", "banana", "grapes"]
num_items = ["three", "two", "one"]
for i in fruits:
  for j in range(0,len(fruits)-1):
    print(i,j)
  print('-- gap --')
  
class Language:
  def __init__(self, name, blah):
    print(self)
    print(name)
    self.blah = blah
    self.name = name
  def getName(self):
    return self.name
  def sendMessage(self):
    return f"My language is {self.name} and I call out {self.blah}"
  
languages = [Language("Python", "🐍"), Language("Javascript", "🥷")]
for language in languages:
  print(language.sendMessage())
  

    