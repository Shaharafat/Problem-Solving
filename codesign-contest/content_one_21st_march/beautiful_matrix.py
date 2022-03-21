if __name__ == "__main__":
  matrix = []
  row = 0 
  column = 0

  # take input make all elements integer
  # get the position of the digit '1'
  for i in range(0,5):
    line = input()
    line = line.split(' ')
    line = list(map(lambda x: int(x), line))
    if (1 in line):
      row = i
      column = line.index(1)
    
    matrix.append(line)

  # Calculate how many moves needed to make the matrix beautiful.
  if(row >= 2):
    row_move = row - 2

  if(row < 2):
    row_move = 2 - row

  if(column >= 2):
    column_move = column - 2

  if(column < 2):
    column_move = 2 - column
    

  print(row_move + column_move)
