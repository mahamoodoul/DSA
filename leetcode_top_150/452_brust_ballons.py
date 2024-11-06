from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrow_count = 1
        arrow_position = points[0][1]

        for start, end in points[1:]:
            if start > arrow_position:
                arrow_count += 1
                arrow_position = end
        return arrow_count
        


points = [[10,16],[2,8],[1,6],[7,12]]
obj = Solution()
output =obj.findMinArrowShots(points)
print(output)