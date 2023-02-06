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
diag1[0,0] = "hello"
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

