class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = list(s)
        longest_substring_length = 0
        substring_list = []

        for idx, item in enumerate(s_list):
            if item not in substring_list:
                substring_list.append(item)
                longest_substring_length = max(
                    longest_substring_length, len(substring_list)
                )
            else:
                index = substring_list.index(item)
                substring_list = substring_list[index + 1 :]
                substring_list.append(item)
                longest_substring_length = max(
                    longest_substring_length, len(substring_list)
                )
        return longest_substring_length
s = Solution()
s.lengthOfLongestSubstring("abcabcbb")
s.lengthOfLongestSubstring("bbbbb")
s.lengthOfLongestSubstring("pwwkew")
s.lengthOfLongestSubstring(" ")
s.lengthOfLongestSubstring("dvdf")
