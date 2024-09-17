from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float('inf')  # Use infinity to represent a large number
        
        # Iterate through the array with the right pointer
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink the window from the left as long as the sum is greater than or equal to the target
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        # If min_length was not updated, return 0, otherwise return the minimal length
        return 0 if min_length == float('inf') else min_length

# Example usage:
obj = Solution()
target = 7
nums = [2, 3, 1, 2, 4, 3]
output = obj.minSubArrayLen(target, nums)
print(output)  # Output: 2