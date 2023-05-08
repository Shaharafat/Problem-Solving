class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = len(nums) - 1
        
        while idx >= 0:
            if idx == 0:
                nums.reverse()
                return
            
            if not (nums[idx] <= nums[idx - 1]):
                pivot = nums[idx - 1]
                idx_data_to_shift = idx - 1
                
                nidx = idx 
                temp_nums = nums[0:idx] + sorted(nums[idx:])
                print('before',temp_nums)
                for i in sorted(nums[idx:]):
                    
                    if i > pivot:
                        print('i',i, 'nidx', nidx, 'pivot', pivot)
                        temp_nums[idx_data_to_shift] = i
                        temp_nums[nidx] = pivot
                        
                        break;
                    
                    nidx = nidx+1
                     
                nums[:] = temp_nums[:]
                
                return nums
            
            idx = idx - 1 
            
            
tests = [
    (
        ([1,2,3],),
        [1,3,2]
    ),
    (
        ([2,3,1],),
        [3,1,2]
    ),
    (
        ([5,9,4,3,1],),
        [9,1,3,4,5]
    ),(
        ([3,2,1],),
        [1,2,3]
    )
]

s = Solution()
s.nextPermutation([3,2,1])
s.nextPermutation([1,2,3])
s.nextPermutation([1,1,5])
s.nextPermutation([1,3,2])
s.nextPermutation([5,9,4,3,1])
s.nextPermutation([5,1,1])