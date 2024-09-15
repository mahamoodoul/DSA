class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i:].startswith(needle):
                return i
        return -1


obj = Solution()
haystack = "kadbutad"
needle = "sad"
output = obj.strStr(haystack, needle)
print(output)