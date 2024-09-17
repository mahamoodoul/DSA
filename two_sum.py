from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the numbers we have seen so far and their indices
        num_map = {}
        
        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            print(num_map)
            # Calculate the complement that would sum up to the target
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in num_map:
                return [num_map[complement], i]
            
            # If not, store the current number and its index in the dictionary
            num_map[num] = i

# Example usage:
obj = Solution()

# Test case 1
nums1 = [2, 11, 11, 7]
target1 = 9
print(obj.twoSum(nums1, target1))  # Output: [0, 1]

