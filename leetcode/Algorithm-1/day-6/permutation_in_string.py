from collections import Counter


class Solution(object):
    def checkInclusion(self, s1, s2):
        result = False

        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len:
            result = False

        s1_count = dict(Counter(s1))
        s2_str = s2[:s1_len]

        s2_count = dict(Counter(s2_str))

        if s1_count == s2_count:
            result = True

        for i in range(s1_len, s2_len):
            if s2_count[s2_str[0]] > 1:
                s2_count[s2_str[0]] -= 1
            else:
                del s2_count[s2_str[0]]

            # adding next element
            s2_str = s2_str[1:] + s2[i]

            if s2_str[-1] in s2_count:
                s2_count[s2_str[-1]] += 1
            else:
                s2_count[s2_str[-1]] = 1

            if s1_count == s2_count:
                result = True

        # print(result)
        return result


s = Solution()
s.checkInclusion("ab", "eidbaooo")
s.checkInclusion("ab", "eidboaooo")
s.checkInclusion("adc", "dcda")
