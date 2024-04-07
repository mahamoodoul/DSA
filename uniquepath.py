from typing import List
# class Solution:
#     def uniquePaths(self, m: int, n: int ) -> int:
#         row = [1] * n

#         for i in range(m- 1):
#             newRow = [1] * n
#             for j in range(n-2,-1,-1):
#                 newRow[j] = newRow[j+ 1] + row[j]
            
#             print(newRow)
#             row = newRow
#         return row[0]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[1 for _ in range(n)] for _ in range(m)]
        print(table)
        for i in range(1, m):
            for j in range(1, n):
                table[i][j] = table[i - 1][j] + table[i][j-1]
        return table[m - 1][n - 1]

m = 3
n = 7
obj = Solution()
print(obj.uniquePaths(m, n))