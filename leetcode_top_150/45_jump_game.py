from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0  # Already at the last index, no jumps needed
        jumps = 0       # To count the number of jumps
        farthest = 0    # The farthest point we can reach in the array
        current_end = 0 # The end of the range we can reach with the current jump
        
        for i in range(n - 1):  # We don't need to check the last index
            # Update the farthest point we can reach
            farthest = max(farthest, i + nums[i])
            
            # If we've reached the end of the current jump range
            if i == current_end:
                jumps += 1          # Make a jump
                current_end = farthest  # Update the range for the next jump
                
                # If we can reach the end, break early
                if current_end >= n - 1:
                    break
        return jumps

# Test the function
obj = Solution()
nums = [4,5,1,3,7,6,1,0,2,3,2,3,1,2,1,1]
output = obj.jump(nums)
print(output)  # Expected output: 2