class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_s = ''.join(e for e in s if e.isalnum()).lower()
        first_index = 0
        last_index = len(string_s) -1
        while first_index < last_index:
            if string_s[first_index] != string_s[last_index]:
                return False
            first_index += 1
            last_index -= 1
        return True




s = "a"
obj = Solution()
output = obj.isPalindrome(s)
print(output)