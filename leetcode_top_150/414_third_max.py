from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct_nums = set(nums)
        sorted_nums = sorted(distinct_nums, reverse=True)
        if len(sorted_nums) >= 3:
            return sorted_nums[2]
        else:
            return sorted_nums[0]




obj = Solution()
nums = [2,1,1,1,2,3,4]
output = obj.thirdMax(nums)
print(output)
