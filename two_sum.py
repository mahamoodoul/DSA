from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for idx, value in enumerate(nums):
            if target - value in values:
                print([values[target - value], idx])
                # values = [values[target - value], idx]
            else:
                print(values)
                values[value] = idx
        print(values)

nums_list = [2,20,11,15]
target = 22
obj = Solution()
print(obj.twoSum(nums_list,target))
