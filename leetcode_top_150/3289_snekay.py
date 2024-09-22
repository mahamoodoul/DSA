from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()
        for i in range(1, len(nums)):
           if nums[i] == nums[i-1]:
               res.append(nums[i])
        return res
       
       


obj = Solution()
nums = [0,3,2,1,3,2]
output = obj.getSneakyNumbers(nums)
print(output)