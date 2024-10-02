from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = ""
        num = 0
        output =[]
        for i in range(len(digits)):
            sum = sum + str(digits[i])
        num = str(int(sum) + 1)
        for j in range(len((num))):
            output.append(int(num[j]))
        return output




obj = Solution()
digits = [9]
output = obj.plusOne(digits)
print(output)

