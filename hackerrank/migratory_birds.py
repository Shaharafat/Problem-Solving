def migratoryBirds(arr:list[int]):
  table = {1:0,2:0,3:0,4:0,5:0}
  max_sightings = 0

  lower_index = max(arr)

  for idx,item in enumerate(arr):
    table[item] += 1 
    if table[item] > max_sightings: max_sightings = table[item]

  for (key,value) in table.items():
    if value == max_sightings :
      lower_index = key
      break

  return lower_index

migratoryBirds([1,4,4,4,5,3])
migratoryBirds([1,2,3,4,5,4,3,2,1,3,4])

