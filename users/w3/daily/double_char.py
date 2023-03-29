

def double_char(string:str)->str:
  new_str = ''
  for letter in string:
    print(f"letter in string: {letter}")
    new_str += letter + "" + letter
  print(new_str)
  return new_str
    
double_char("Hi-There")