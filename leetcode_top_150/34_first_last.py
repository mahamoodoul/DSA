from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        if len(nums) == 1 and target == nums[0]:
            return [0,0]
        for i in range(len(nums)):
            if target == nums[i]:
                res.append(i)
        if len(res) > 2:
            return [res[0], res[-1]]
        elif len(res) == 2:
            return res
        elif len(res) == 1:
            res.append(res[0])
            return res
        else:
            return [-1,-1]

obj = Solution()
nums = [1,3]
target = 1
output = obj.searchRange(nums, target)
print(output)