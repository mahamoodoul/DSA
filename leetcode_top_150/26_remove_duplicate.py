from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize the write pointer `k`
        k = 1  # Start at 1 because the first element is always unique
        
        # Iterate over the list starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the previous one, it is unique
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]  # Place the unique element at index `k`
                print(nums)
                k += 1  # Increment the write pointer
        
        return k  # `k` is the new length of the array with unique elements


# Example Usage
sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
k = sol.removeDuplicates(nums)
print(f"New length: {k}, Modified nums: {nums[:k]}")