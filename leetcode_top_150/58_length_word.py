from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        count = 0
        flag = True
        for i in range(n-1,-1,-1):
            if s[i] != " ":
                count += 1
                flag = False
            else:
                if flag == False:
                    return count
        return count
        
            
            






s = "luffy is still joyboy"
obj = Solution()
output = obj.lengthOfLastWord(s)
print(output)