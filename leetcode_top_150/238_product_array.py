from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize the answer array with 1s
        answer = [1] * n
        # Compute the prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        # Compute the suffix products and multiply it with the prefix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer

# Example usage:
sol = Solution()
nums = [1, 2, 3, 4]
output = sol.productExceptSelf(nums)
print(output)  # Output: [24, 12, 8, 6]