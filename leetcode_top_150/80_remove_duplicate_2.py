from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)  # If there are fewer than 3 elements, no need to remove duplicates
        # Initialize the write pointer `k`
        k = 2  # Start at 2 because the first element is always unique or duplicate
        # Iterate over the list starting from the third element
        for i in range(2, len(nums)):
            # If nums[i] is different from nums[k-2], it means nums[i] can be included
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]  # Place the unique element at index `k`
                k += 1  # Increment the write pointer
        return k  # `k` is the new length of the array with unique elements


# Example Usage
sol = Solution()
nums = [0,0,0,1,1,1,1,2,3,3,3,3,3,3,3,4,4,4]
k = sol.removeDuplicates(nums)
print(f"New length: {k}, Modified nums: {nums[:k]}")