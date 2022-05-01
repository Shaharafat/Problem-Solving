import math


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1
        while lower <= upper:
            mid = math.ceil((lower + upper) / 2)

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                upper = mid - 1
            else:
                lower = mid + 1
        return -1


s = Solution()
print(
    s.search(
        [-1, 0, 3, 5, 9, 12],
        0,
    )
)
