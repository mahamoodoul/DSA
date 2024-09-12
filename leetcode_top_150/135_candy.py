from typing import List
# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         total = len(ratings)
#         for i in range(len(ratings)):
#             if i == 0:
#                 if (ratings[i] > ratings[i+1]):
#                     total += 1
#             elif i == len(ratings)-1:
#                 if (ratings[i] > ratings[i -1]):
#                     total += 1
#             else:
#                 if (ratings[i] > ratings[i+1]) or (ratings[i] > ratings[i-1]):
#                     total += 1
#         return total

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        
        # Initialize candies array with 1 for each child (each child gets at least 1 candy)
        candies = [1] * n
        
        # Left to right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Right to left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        # Sum up all candies
        return sum(candies)




obj = Solution()
ratings = [1,2,87,87,87,2,1]
output = obj.candy(ratings)
print(output)