# class Solution(object):
#     def longestPalindrome(self, s: str) -> str:
#         result: str = ""
#         result_length: int = 0

#         for i in range(len(s)):
#             l, r = i, i

#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 if (r - l + 1) > result_length:
#                     result = s[l : r + 1]
#                     result_length = r - l + 1
#                 l -= 1
#                 r += 1

#             l, r = i, i + 1

#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 if (r - l + 1) > result_length:
#                     result = s[l : r + 1]
#                     result_length = r - l + 1
#                 l -= 1
#                 r += 1
#         return result
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result: str = ""
        result_length: int = 0

        for i in range(len(s)):
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                # result = s[l] + result + s[r]
                # if len(result) > result_length:
                #     result_length = len(result)
                if (r - l + 1) > result_length:
                    result = s[l : r + 1]
                    result_length = r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                # result = s[l] + result + s[r]
                # if len(result) > result_length:
                #     result_length = len(result)
                if (r - l + 1) > result_length:
                    result = s[l : r + 1]
                    result_length = r - l + 1
                l -= 1
                r += 1
        return result

# s = Solution()
# print(s.longestPalindrome("ac"))
tests = [
    (
        
    ("babad",),
    "bab",
    )
]
