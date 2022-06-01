# Remove Space (L)
# FORMULA: sqrt(L) <= row <= column
# rows * column >= L
#   

# STEPS
# - Remove spaces
# - Join and make it a single string
# - Get the sqrt value
# - Determine the row and columns count
#     - If floor and ceil is equal then use the value to calc row and column
#     - If floor * ceil >= L then use them as row and column
#     - Else use ceil * ceil as row and column
# - Split it as column size

import math


def encryption(s):
  # remove space
  s = s.split(' ')
  s = ''.join(s)

  s_length = len(s)
  sqrt = math.sqrt(s_length)
  sqrt_ceil = math.ceil(sqrt)
  sqrt_floor = math.floor(sqrt)
  rows = None
  columns = None

  # determine row and columns count
  if sqrt_ceil == sqrt_floor:
    rows = columns = sqrt_ceil
  elif sqrt_ceil * sqrt_floor >= s_length:
    columns = sqrt_ceil
    rows = sqrt_floor
  else:
    columns = sqrt_ceil
    rows = sqrt_floor
  

  string  = ''
  for i in range(0, columns):
    j = i
    while True:
      if(j < s_length):
        string += s[j]
        j += columns
      else:
        string += ' '
        break

  return string


  print(rows, columns)
