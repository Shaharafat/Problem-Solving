import math


def isBadVersion(n):
  if n == 4 or n == 5 or n == 6 or n==7 or n == 8 or n == 9 or n == 10 or n == 11 or n ==12 or n == 13 or n == 14 or n == 15:
    return True
  else:
    return False
  
def firstBadVersion( n: int) -> int:
      
    lower = 1
    upper = n
    mid = upper

    while lower <= upper:
      mid = math.ceil((lower + upper) / 2)

      isBad = isBadVersion(mid)

      if not isBad: 
        lower = mid + 1
      else: 
        upper = mid - 1
         
    return lower

result = firstBadVersion(11)
print(result)
