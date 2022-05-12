def saveThePrisoner(n, m, s):
  res = (s + m - 1) % n
  if res == 0:
    return n
  else:
    return res 

saveThePrisoner(5,2,1)
saveThePrisoner(3,7,3)
saveThePrisoner(4,6,2)
saveThePrisoner(7, 19, 2)
