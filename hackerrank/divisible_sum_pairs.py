def divisibleSumPairs(n:int,k:int,ar:list[int]):
  # Using sliding window algorithm
  count = 0
  for idx in range(0,n):
    for i in range(idx+1, n):
      if (ar[idx] + ar[i]) % k == 0:
        count += 1
        
    
  return count

print(divisibleSumPairs(6,3,[1,3,2,6,1,2]))
print(divisibleSumPairs(6,5,[1,2,3,4,5,6]))
