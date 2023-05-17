from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left: int = self.binarySearch(nums, target)
        right: int = self.binarySearch(nums, target, False)

        return [left, right]

    def binarySearch(
        self, list_of_nums: List[int], target: int, leftPortion: bool = True
    ) -> int:

        l: int = 0
        r: int = len(list_of_nums) - 1
        i: int = -1
        while l <= r:

            mid: int = (l + r) // 2

            if target > list_of_nums[mid]:
                l = mid + 1
            elif target < list_of_nums[mid]:
                r = mid - 1
            else:
                i = mid

                if leftPortion:
                    r = mid - 1
                else:
                    l = mid + 1

        return i


# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# tests = [(([5, 7, 7, 8, 8, 10], 8), [3, 4])]

s = Solution()
result = s.searchRange([5, 7, 7, 8, 8, 10], 8)
print(result)
