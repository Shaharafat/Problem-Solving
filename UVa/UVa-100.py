
cache = {}
def calculate_cycle(x,y):
  max = -1

  for i in range(x, y+1):
    n = i
    cycle_count = 1
    if n in cache:
      cycle_count = cache[n]
    else:
      while n != 1:  
        cycle_count += 1
        if n % 2 == 0:
          n = n//2
        else :
          n = 3 * n + 1

    cache[i] = cycle_count
    if cycle_count > max:
      max = cycle_count
  return max


if __name__ == '__main__':
  while True:
    try:
      x, y = map(int, input().split()[:2])
      lower_bound = x if x < y else y
      upper_bound = x if x > y else y
      max = calculate_cycle(lower_bound, upper_bound)
      print(f'{x} {y} {max}')
    except EOFError:
      break
