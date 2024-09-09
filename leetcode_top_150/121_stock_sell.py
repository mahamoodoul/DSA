from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(0, len(prices)-1):
            for j in range(i+ 1, len(prices)):
                diff = prices[j] - prices[i]
                print("diff", diff)
                if diff < 0:
                    diff = 0
                max_profit = max(max_profit,diff)
        return max_profit
            









# Example Usage
sol = Solution()
prices = [1,2]
k = sol.maxProfit(prices)
print(k)