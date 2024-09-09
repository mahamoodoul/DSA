from typing import List
from collections import defaultdict

# Hash Map Approach (Counting Frequencies)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Dictionary to store the frequency of each element
        freq = defaultdict(int)
        result = []
        n = len(nums)

        
        
        # Count the frequency of each element
        for num in nums:
            freq[num] += 1
        print(freq)
        # Check which elements appear more than n // 3 times
        for key, value in freq.items():
            if value > n // 3:
                result.append(key)
        
        return result

# one way solution

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         candidate1, candidate2 = None, None
#         vote1, vote2 = 0, 0
#         for num in nums:
#             if candidate1 == num:
#                 vote1 += 1
#             elif candidate2 == num:
#                 vote2 += 1
#             elif vote1 == 0:
#                 candidate1, vote1 = num, 1
#             elif vote2 == 0:
#                 candidate2, vote2 = num, 1
#             else:
#                 vote1 -= 1
#                 vote2 -= 1
#         result = []
#         for candidate in [candidate1, candidate2]:
#             if nums.count(candidate) > len(nums) // 3:
#                 result.append(candidate)
#         return result

    
# Example Usage
sol = Solution()
nums = [8,8,8,8]
k = sol.majorityElement(nums)
print(k)