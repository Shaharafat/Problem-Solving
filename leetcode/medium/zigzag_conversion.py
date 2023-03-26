class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strObj = {}

        # TODO: Create some list of strings equal to numRows
        for i in range(1, numRows + 1):
            strObj[i] = list()

        # TODO: loop over 0 - numRows until the string completes
        stridx = 0
        idx = 0
        increase = True

        if numRows == 1:
          return s
        while True:
            if idx == numRows:
                increase = False if increase else True
            elif idx == 1:
                increase = True

            if increase:
                idx += 1
            else:
                idx -= 1

            if stridx < len(s):
                try:
                    strObj[idx].append(str(s[stridx]))
                    stridx += 1
                except IndexError:
                    continue
            else:
                break

        total = []

        # join all lists
        for (key, val) in strObj.items():
            total += strObj[key]
        return "".join(total)


c = Solution()
c.convert("PAYPALISHIRING", 3)
