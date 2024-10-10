from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix)-1
        while left < right:
            for i in range(right - left):
                top, bottom = left, right
                #save top left
                topLeft = matrix[top][left + i]

                #move bottom left to top left
                matrix[top][left+i] = matrix[bottom-i][left]

                #move bottom right to into bottom left
                matrix[bottom-i][left] = matrix[bottom][right-i]
                #move top right to bottom right 
                matrix[bottom][right-1] = matrix[top + i][right]
                #move top left to top right
                matrix[top+i][right] = topLeft
            left += 1
            right -= 1






obj = Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
obj.rotate(matrix)
print(matrix)
