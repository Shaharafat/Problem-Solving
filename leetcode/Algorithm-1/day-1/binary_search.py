import math


def binary_search(nums, target: int) -> int:
    """
    Binary search
    """
    lower = 0
    upper = len(nums) - 1

    while lower <= upper:
        mid = math.ceil((lower + upper) / 2)
        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            upper = mid - 1

        if nums[mid] < target:
            lower = mid + 1

    return -1


result = binary_search([-1, 0, 3, 5, 9, 12], 10)
print(result)
