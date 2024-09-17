from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        first_index = 0
        last_index = len(height) - 1

        while first_index < last_index:
            # Calculate the width
            width = last_index - first_index
            # Calculate the water based on the smaller height
            water = min(height[first_index], height[last_index]) * width
            # Update the maximum water found so far
            max_water = max(max_water, water)

            # Move the pointer with the smaller height
            if height[first_index] < height[last_index]:
                first_index += 1
            else:
                last_index -= 1

        return max_water





obj = Solution()
height = [1,1]
output = obj.maxArea(height)
print(output)