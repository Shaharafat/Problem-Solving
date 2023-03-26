# Author : Shah Arafat
# Platform: Leetcode
# Problem Name: Reverse Integer
# Level : Medium
# Date: 26th Match 2k23


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x

        isNegative = False

        if x < 0:
            isNegative = True

        y = abs(x)
        reversed = ""
        passedDigit = False
        while y != 0:
            val = y % 10
            if val != 0:
                reversed = reversed + str(val)
                passedDigit = True
            elif passedDigit:
                reversed = reversed + str(val)

            y = y // 10

        if isNegative:
            reversed = "-" + reversed

        upperlimit = 2**31 - 1
        lowerlimit = -(2**31)
        if int(reversed) > upperlimit or int(reversed) < lowerlimit:
            return 0
        else:
            return int(reversed)


s = Solution()
p = s.reverse(901000)
print(p)
