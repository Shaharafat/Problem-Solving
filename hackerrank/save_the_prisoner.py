def saveThePrisoner(n, m, s):
  # first_covered = n - s + 1 
  # remaining = n - first_covered
  # print(first_covered,remaining)


  # if m - first_covered :
  #   return first_covered

  # if n > m:
  #   return m + s - 1
  # else:
  #   return m % n + s - 1
  print((m % n )+ s - 1)

saveThePrisoner(5,2,1)
saveThePrisoner(3,7,3)
saveThePrisoner(4,6,2)
saveThePrisoner(7, 19, 2)
