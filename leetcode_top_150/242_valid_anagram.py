from typing import List
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # hash_letter = {}
        # for i in range(len(s)):
        #     count = 1
        #     if s[i] in hash_letter:
        #         hash_letter[s[i]] = hash_letter[s[i]] + 1
        #     else:
        #         hash_letter[s[i]] = count
        # hash_letter_2 = {}
        # for i in range(len(t)):
        #     count = 1
        #     if t[i] in hash_letter_2:
        #         hash_letter_2[t[i]] = hash_letter_2[t[i]] + 1
        #     else:
        #         hash_letter_2[t[i]] = count

        # if hash_letter == hash_letter_2:
        #     return True
        # else:
        #     return False
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False
        char_count ={}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        for char in t:
            char_count[char] = char_count.get(char, 0) -1
        for count in char_count.values():
            if count != 0:
                return False
        return True






obj = Solution()
s = "anagram"
t = "nagaram"
output = obj.isAnagram(s,t)
print(output)