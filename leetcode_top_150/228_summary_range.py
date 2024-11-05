from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        if not nums:
            return range
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]+1:
                if start == nums[i-1]:
                    ranges.append(f"{start}")
                else:
                    ranges.append(f"{start}->{nums[i - 1]}")
                start =  nums[i]

                
        if start == nums[-1]:
            ranges.append(f"{start}")
        else:
            ranges.append(f"{start}->{nums[-1]}")

        return ranges
        





nums = [0,1,2,3,4,5,6,7]
obj = Solution()
output = obj.summaryRanges(nums)
print(output)