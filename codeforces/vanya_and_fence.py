def calculate_min_width(height_of_fence, list_of_height):
  width = 0
  for height in list_of_height:
    if height > height_of_fence:
      width += 2
    else:
      width += 1
  
  return width


if __name__ == '__main__':
  n,h = list(map(lambda i : int(i), input().split(' ')))
  list_of_height =list(map(lambda i : int(i), input().split(' '))) 

  result = calculate_min_width(h, list_of_height)
  print(result)
