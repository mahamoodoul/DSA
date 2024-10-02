from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # sum = ""
        # num = 0
        # output =[]
        # for i in range(len(digits)):
        #     sum = sum + str(digits[i])
        # num = str(int(sum) + 1)
        # for j in range(len((num))):
        #     output.append(int(num[j]))
        # return output
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits




obj = Solution()
digits = [9]
output = obj.plusOne(digits)
print(output)

