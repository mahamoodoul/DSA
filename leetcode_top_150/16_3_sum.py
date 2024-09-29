from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        for i in range(n-2):
            left, right = i + 1, n-1
            while left < right:
                output = nums[i] + nums[left] + nums[right]
                if output == target:
                    return output
                if abs(output - target) < abs(closest_sum - target):
                    closest_sum = output
                if output < target:
                    left += 1
                else:
                    right -= 1
        return closest_sum
            




obj = Solution()
nums = [-1,2,1,-4]
target = 1
output = obj.threeSumClosest(nums, target)
print(output)