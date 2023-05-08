class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = len(nums) - 1
        while idx >= 0:
            # print(nums[idx])
            if not (nums[idx] < nums[idx - 1]) and (idx - 1 >= 0):
                pivot = nums[idx - 1]
                print(pivot, 'idx', idx-1)
                # return
            
            idx = idx - 1 
            # print(nums[idx])
            
            
tests = [
    # (
    #     ([1,2,3],),
    #     [1,3,2]
        
    # ),
    (
        ([2,3,1],),
        [3,1,2]
    )
]

s = Solution()
s.nextPermutation([2,3,1])