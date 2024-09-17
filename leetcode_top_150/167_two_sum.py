from typing import List

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         num = numbers[0]
#         output = [0,0]
#         for i in range(1, len(numbers)):
#             find = target - num
#             if find in numbers[i:]:
#                 output[0] = (numbers.index(num)+1)
#                 output[1] = (numbers[i:].index(find)+ i + 1)
#                 break
#             else:
#                 num = numbers[i]
#         return output
    
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                return [left + 1, right + 1]



obj = Solution()
numbers = [5,25,75]
target = 100
output = obj.twoSum(numbers, target)
print(output)