from typing import List

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = [""] * numRows
        if numRows == 1:
            return s
        flag = False
        i = 0
        for ch in s:
            ans[i] += ch
            if (i == 0  or numRows-1 == i):
                flag = not flag
            if flag:
                i = i + 1
            else:
                i = i - 1
        zigzag = ''.join(ans)
        return zigzag
        
            




obj = Solution()
s = "PAYPALISHIRING"
numRows = 4
output = obj.convert(s, numRows)
print(output)