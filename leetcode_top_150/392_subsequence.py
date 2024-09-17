class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Edge case: if s is an empty string, it's always a subsequence
        if not s:
            return True
        
        # Initialize a pointer for string s
        s_index = 0
        
        # Loop through each character in string t
        for char in t:
            # If the current character in t matches the character in s at s_index
            if char == s[s_index]:
                # Move to the next character in s
                s_index += 1
                
            # If we have matched all characters in s, return True
            if s_index == len(s):
                return True
        
        # If not all characters were matched, return False
        return False


# Example usage
s = "ab"
t = "baab"
obj = Solution()
output = obj.isSubsequence(s, t)
print(output)