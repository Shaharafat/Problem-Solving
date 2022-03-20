
def searchInsert(nums : list[int], target: int):
  lower = 0
  upper = len(nums) - 1

  while lower <= upper:
    mid = (lower + upper) // 2
    if(nums[mid] == target):
      return mid

    if(nums[mid] > target):
      upper = mid - 1
    else: 
      lower = mid + 1
    
  return lower

result = searchInsert([1,3,5,6], 4)
print(result)
