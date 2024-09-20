from typing import List
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
            # Count the frequency of each character in both strings
        magazine_count = Counter(magazine)
        ransomNote_count = Counter(ransomNote)
        print(type(ransomNote_count))
        # Check if each character in ransomNote can be constructed from magazine
        for char, count in ransomNote_count.items():
            print(char, count)
            if magazine_count[char] < count:
                return False
        return True



obj = Solution()
ransomNote = "aa"
magazine = "aab"
output = obj.canConstruct(ransomNote, magazine)
print(output)