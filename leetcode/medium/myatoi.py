# Author: Shah Arafat
# Platform: Leetcode
# Problem Name: MyAtoi
# Level : Medium
# URL: https://leetcode.com/problems/string-to-integer-atoi/
# Date: 2023-03-26 16:06:13

import re


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        reg = r"[0-9]"
        isPositive = True

        if s == "":
            return 0

        if s[0] == "+" or s[0] == "-":
            if s[0] == "-":
                isPositive = False

            s = s[1:]

        final_int = ""
        for char in s:
            if re.match(reg, char):
                # print(char)
                final_int = final_int + char
            else:
                break
        print("s", s)
        if final_int == "":
            return 0
        if not isPositive:
            final_int = "-" + final_int

        lower_limit = -(2**31)
        upper_limit = 2**31 - 1

        if int(final_int) > upper_limit:
            return upper_limit
        if int(final_int) < lower_limit:
            return lower_limit

        return int(final_int)


s = Solution()

# print(s.myAtoi("   -42"))
print(s.myAtoi(".1"))
# print(s.myAtoi("4193 with words"))
