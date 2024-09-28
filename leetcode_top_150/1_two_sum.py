from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        output= []
        for idx, value in enumerate(nums):
            diff = target - value
            if diff in prevMap:
                output = [prevMap[diff], idx]
            prevMap[value] = idx
            print(prevMap)
        return output




obj = Solution()
nums = [2,7,11,15]
target = 9
output = obj.twoSum(nums, target)
print(output)