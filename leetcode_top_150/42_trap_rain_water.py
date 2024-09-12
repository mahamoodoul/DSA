from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        trap_water = 0
        n = len(height)
        left_max = [0]* n
        right_max = [0] * n
        # calculate left max
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i-1])
        # calculate right max
        right_max[n-1] = height[n-1]
        for i in range(n-2,-1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        
        for i in range(n):
            trap_water = trap_water + (min(left_max[i], right_max[i]) -height[i])
        return trap_water


height = [0,1,0,2,1,0,1,3,2,1,2,1]
obj = Solution()
output = obj.trap(height)
print(output)