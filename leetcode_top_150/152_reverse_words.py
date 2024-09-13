from typing import List
class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        first_index = 0
        last_index = len(s_list) -1
        while first_index < last_index:
            s_list[first_index], s_list[last_index] = s_list[last_index], s_list[first_index]
            first_index += 1
            last_index -= 1
        output = ""
        if not len(s_list) <= 0:
            output = s_list[0]
            for i in  range(1, len(s_list)):
                output += " " + s_list[i]  
        return output







s ="the sky is blue"
obj = Solution()
output = obj.reverseWords(s)
print(output)