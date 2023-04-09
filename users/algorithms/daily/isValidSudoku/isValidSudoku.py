def duplicates(anArray:list)->bool:
  obj = {}
  dotless = [num for num in anArray if num!='.']
  # print(f"dotless:{dotless}")
  for num in dotless:
    # print(f"num:{num}")
    if num in obj:
      obj[num] += 1
    else:
      obj[num] = 1
  
  dupes = []
  for k,v in obj.items():
    # print(f"value:{k}")
    if v > 1:
      dupes.append(k)
      
  return dupes
    
a = [1,2,3]
b = [1,2,1,2,3]
# print(f"has dupes? {duplicates(b)}")

def isValidSudoku(board)->bool:
  '''
  board = [
     ["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]
  ]
  '''
  print(f"board\n{board}")
  # check by rows
  for i in range(len(board)):
    # print(f"row:{board[i]} ith:{i}")
    has_dupes = True if len(duplicates(board[i])) > 0 else False
    print(f"does ROW {i}th have dupes? {has_dupes}")
    if has_dupes == True:
      return False
  # check by cols
  
  temp = []
  for i in range(len(board)):
    for col in range(len(board[i])):
      if len(temp)==9:
        temp = []
      temp.append(board[col][i])
    has_dupes = True if len(duplicates(temp)) > 0 else False
    print(f"have duplicates ?: {has_dupes}") 
    temp = []
  # check by 3 X 3 (the first 3 rows' group of three elements)
  int_arr = [[int(num) if num.isdigit() else -1 for num in row] for row in board]
  three_by_three = []
  for i in range(0,9,3): # rows
    for j in range(0,9,3): # cols
      for k in range(i, i+3): # rows
        for l in range(j, j+3):
          print(int_arr[k][l], end=" ")
          
          three_by_three.append(int_arr[k][l])  
          
        print(" ")
          
      print(" === === ")
      print(f"three by three: {three_by_three}")
      while -1 in three_by_three:
        three_by_three.remove(-1)
      has_dupes = True if len(duplicates(three_by_three)) > 0 else False
      print(f"have duplicates ?: {has_dupes}")
      if len(three_by_three) != 0:
          three_by_three = []
      if has_dupes == True:
        return False
  return True
        
      
            
      
      
      
      



board = [
     ["5","3",".",".","7",".",".","3","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,["7","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]
  ]

print(isValidSudoku(board))

