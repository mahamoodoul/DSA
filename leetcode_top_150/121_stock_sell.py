from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')  # Start with a very large number
        
        # Loop through each price
        for price in prices:
            # Update the minimum price if the current price is lower
            if price < min_price:
                min_price = price
            # Calculate the profit if we sell at the current price
            profit = price - min_price
            # Update the maximum profit if this profit is higher than the previous max profit
            if profit > max_profit:
                max_profit = profit
                
        return max_profit
            









# Example Usage
sol = Solution()
prices = [1,2]
k = sol.maxProfit(prices)
print(k)