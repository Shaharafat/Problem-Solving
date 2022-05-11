import math


class Solution:
    # def binary_search(self, nums: list[int], target):
    #     lower = 0
    #     upper = len(nums) - 1

    #     while lower <= upper:
    #         mid = (lower + upper) // 2
    #         print("mid", nums[mid])
    #         if target < 0:
    #             if nums[mid] == 0:
    #                 return mid + 1

    #         if nums[mid] <= target:
    #             return mid + 1

    #         if nums[mid] > target:
    #             upper = mid - 1
    #         if nums[mid] < target:
    #             lower = mid + 1

    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # smaller_then_target_index = self.binary_search(numbers, target)
        # numbers = numbers[0 : int(smaller_then_target_index + 1)]
        # print("numbers", numbers)

        lower = 0
        upper = len(numbers) - 1
        while lower < upper:
            if numbers[lower] + numbers[upper] == target:
                return [lower + 1, upper + 1]

            if numbers[lower] + numbers[upper] > target:
                upper = upper - 1
            if numbers[lower] + numbers[upper] < target:
                lower = lower + 1


s = Solution()
# print(s.twoSum([1, 2, 3, 4, 6, 7], 5))
# print(s.twoSum([-1, 0], -1))
# print(s.twoSum([2, 3, 4], 6))
print(s.twoSum([3, 24, 50, 79, 88, 150, 345], 200))
