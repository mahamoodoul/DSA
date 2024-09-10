from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy, sell = 0,0
        total = 0
        # Loop through each price
        for i in range( 0 , len(prices) - 1 ):
            buy = prices[i]
            sell = prices[i+1]
            max_profit = sell - buy
            if max_profit < 0:
                max_profit = 0
            total = total + max_profit
        return total


obj = Solution()
prices = [7,6,4,3,1]
output = obj.maxProfit(prices)
print(output)  # Output will be the sorted merged list