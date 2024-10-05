from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not 
        return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        left = 0
        right = len(nums)-1
        while left < right:
            if nums[right] > 0:
                hold = nums[left]
                nums[left] = nums[right]
                nums[right] = hold
                right -= 1
                left += 1
            else:
                right -= 1
                continue




obj = Solution()
nums = [0]
output = obj.moveZeroes(nums)
print(nums)
