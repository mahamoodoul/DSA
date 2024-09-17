from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = []
        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            lo, hi = i + 1, n-1
            while lo <  hi:
                three_sum  = nums[i] +  nums[lo] + nums[hi]
                if three_sum == 0:
                    answer.append([nums[i], nums[lo], nums[hi]])
                    lo, hi = lo + 1, hi - 1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi -= 1
                elif three_sum < 0:
                    lo += 1
                else:
                    hi -= 1
        return answer
            





nums = [-1,0,1,2,-1,-4]
obj = Solution()
output = obj.threeSum(nums)
print(output)