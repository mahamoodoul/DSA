from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        self.reverse(nums,0, n-1)
        # self.reverse(nums, 0, k -1)
        # self.reverse(nums, k, n-1)


    
    def reverse(self, nums:List[int], first:int, last:int) -> None:
        while first < last:
            nums[first], nums[last] = nums[last], nums[first]
            first += 1
            last -= 1




obj = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
obj.rotate(nums, k)
print(nums)  # Output will be the sorted merged list