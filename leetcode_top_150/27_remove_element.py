from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # This will track the count of elements not equal to val
        
        # Iterate through each element in nums
        for i in range(len(nums)):
            if nums[i] != val:
                # Overwrite the element at index `k` with the current element
                nums[k] = nums[i]
                k += 1  # Move the write pointer forward
        return k  # The count of elements not equal to `val


# nums = [3,2,2,3]
# val = 3
sol = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2

k = sol.removeElement(nums, val)
print(f"New length: {k}, Modified nums: {nums[:k]}")
        