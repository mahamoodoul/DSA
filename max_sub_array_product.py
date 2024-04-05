from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        print(res)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
            tmp = curMax * n
            curMax = max(n*curMax, n*curMin, n)
            curMin = min(tmp, n*curMin, n)
            res = max(res, curMax)
        return res


nums = [2, -1, 3, 4, -1, 2, 1, 5, 4]
obj = Solution()
print(obj.maxSubArray(nums))
