from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #sorting solutions
        # if not nums:
        #     return 0
        # nums.sort()
        # longest_sequence = 1
        # current_sequence = 1
        # for i in range (1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         continue
        #     if nums[i] == nums[i-1]+1:
        #         current_sequence += 1
        #     else:
        #         longest_sequence = max(longest_sequence, current_sequence)
        #         current_sequence = 1
        # return max(longest_sequence, current_sequence)
        num_set = set(nums)
        longest_sequence = 0
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_sequence = 1
            else:
                continue
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1
            longest_sequence = max(longest_sequence, current_sequence)
        return longest_sequence

      

nums = [0,3,7,2,5,8,4,6,0,1]
obj = Solution()
output = obj.longestConsecutive(nums)
print(output)