from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        results = []
        s = s + " "

        # loop over queries array to find result fot each 2D index

        for query in queries:
            str_to_check = s[query[0] : query[1] + 1]
            print(str_to_check)


s = Solution()
s.platesBetweenCandles("**|**|***|", [[2, 5], [5, 9]])
