if __name__ == "__main__":
  line = input()

  [n, k] = line.split(' ')
  n = int(n)
  k = int(k)

  while k:
    if ( n % 10 == 0):
      n = n / 10
    else:
      n = n - 1

    k -= 1 

  print(int(n))  
  
  
