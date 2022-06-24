from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums: return False
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True

        return False

nums = [7, 1, 10, 3, 7, 4]
obj = Solution()
print(obj.containsDuplicate(nums))