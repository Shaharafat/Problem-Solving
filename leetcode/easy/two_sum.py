class Solution:
    def twoSum(self, nums:list[int], target: int) ->list[int]:
        # Using sliding window algorithm
        indices = []
        for idx,item in enumerate(nums):
          indices = [idx]
          for i in range(idx+1, len(nums)):
            if nums[indices[0]] + nums[i] == target:
              indices.append(i) 
              return indices


s = Solution()
# print(s.twoSum([2,7,11,15],9))
# print(s.twoSum([3,2,4],6))
# print(s.twoSum([3,3],6))

class Solution_Efficient:
    def twoSum(self, nums:list[int], target: int) ->list[int]:
        indices = {}

        for idx,item in enumerate(nums):
          wanted = target - item

          if wanted in indices:
            return [indices[wanted], idx]

          indices[item] = idx
      
s2 = Solution_Efficient()
s2.twoSum([2,7,11,15],9)
s2.twoSum([3,2,4],6)
s2.twoSum([3,3],6)
