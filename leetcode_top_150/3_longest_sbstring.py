from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        unique_set = set()
        left = 0
        for right in range( len(s)):
            while s[right] in unique_set:
                unique_set.remove(s[left])
                left += 1
            unique_set.add(s[right])
            max_length = max( max_length, right - left + 1)
        return max_length




obj = Solution()
s = "ckilbkd"
output = obj.lengthOfLongestSubstring(s)
print(output)
