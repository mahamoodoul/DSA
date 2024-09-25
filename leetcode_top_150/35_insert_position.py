from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = 0
        for i in range(len(nums)):
            if target == nums[i]:
                ans = i
                break
            elif target < nums[i]:
                ans = i
                break
            else:
                ans = i + 1
        return ans



obj = Solution()
nums = [1,3,5,6]
target = 7
output = obj.searchInsert(nums, target)

print(output)