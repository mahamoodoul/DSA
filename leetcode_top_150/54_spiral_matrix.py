from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix:
           return result
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        while top <= bottom and left <= right:
            # Traverse from left to right across the top row
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1
            # Traverse top to bottom from right side
            for i in range(top, bottom +1):
                result.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                # Traverse from right to left across the bottom row
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                # Traverse bottom to top from left side
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                    left += 1
        return result
           




obj = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
output = obj.spiralOrder(matrix)
print(output)