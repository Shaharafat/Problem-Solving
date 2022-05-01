class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = k
        if len(nums) < j:
            j = j % len(nums)
        if j == 0:
            pass

        else:
            temp = nums[0:-j]
            nums[0:-j] = nums[-j:]
            nums[-j:] = temp
        print(nums)


s = Solution()
s.rotate([1], 0)
