class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]

        # lower = 0
        # upper = len(s) - 1

        # while lower < upper:
        # temp = s[lower]
        # s[lower] = s[upper]
        # s[upper] = temp

        # lower += 1
        # upper -= 1
