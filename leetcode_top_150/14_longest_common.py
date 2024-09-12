from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Start with the first string as the prefix
        prefix = strs[0]

        # Compare prefix with each string in the list
        for s in strs[1:]:
            # Reduce the prefix length until it matches the start of string 's'
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # Remove the last character from prefix
                if not prefix:
                    return ""
        return prefix





strs = ["flower","flow","flight"]
obj = Solution()
output = obj.longestCommonPrefix(strs)
print(output)