# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         count = 0
#         for idx, value in enumerate(nums):
#             if value == 0:
#                 count = count + 1
#                 nums.remove(nums[idx])

#         nums = nums + [0] * count
#         print(nums)


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lower = 0
        upper = len(nums) - 1
        while lower <= upper:
            if nums[lower] == 0:
                nums.remove(nums[lower])
                nums.append(0)
                upper -= 1
            else:
                lower += 1


s = Solution()
s.moveZeroes([1, 2, 0, 3, 4, 0, 8, 0])
