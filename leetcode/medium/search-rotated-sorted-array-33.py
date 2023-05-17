from typing import List

# O(n) solution
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         for idx, value in enumerate(nums):
#             if value == target:
#                 return idx

#         return -1


# o(log n) solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            print(l, r, mid)

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]:

                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:

                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1


tests = [(([4, 5, 6, 7, 0, 1, 2], 0), 4)]
s = Solution()
v = s.search([4, 5, 6, 7, 0, 1, 2], 0)
print(v)
