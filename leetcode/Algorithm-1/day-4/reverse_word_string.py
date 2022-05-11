class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split(" ")
        final_string = ""
        for i in range(0, len(a)):
            final_string += a[i][::-1]

            if i != len(a) - 1:
                final_string += " "

        return final_string


s = Solution()
s.reverseWords("a quick brown")
