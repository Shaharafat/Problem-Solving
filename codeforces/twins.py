if __name__ == "__main__":
  n = int(input())
  coins = list(map(lambda i : int(i), input().split(' ')))
  coins = sorted(coins, reverse=True)

  total_value = 0
  coin_count = 0

  for value in coins:
    total_value += value
  
  count = 0
  value = 0

  for val in coins:
    value += val
    count += 1

    if value > total_value / 2: 
      print(count)
      break
    
