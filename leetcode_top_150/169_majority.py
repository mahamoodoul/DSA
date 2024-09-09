from typing import List

# one way solution

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         # Return the element at the middle index
#         return nums[len(nums) // 2]

# another Solution

# The Boyer-Moore Voting Algorithm is a very efficient algorithm to find the majority element in an array 
# (i.e., an element that appears more than ⌊n / 2⌋ times). This algorithm works in O(n) time and uses O(1) 
# space, making it highly efficient


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        vote = 0
        for num in nums:
            if vote == 0:
                candidate = num
            if num == candidate:
                vote += 1
            else:
                vote -= 1
          # Optional second pass: Verify the candidate is indeed the majority element
        # This is needed if it's not guaranteed that the majority element exists
        if nums.count(candidate) > len(nums) // 2:
            return candidate
        
        return -1  # If no majority element exists, though it's guaranteed by the problem statement


    
# Example Usage
sol = Solution()
nums = [2,2,1,1,1,2,2,3,3,2,2]
k = sol.majorityElement(nums)
print(k)