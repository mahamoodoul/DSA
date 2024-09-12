from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        total_cost = 0
        current_balance = 0
        start_station = 0
        
        for i in range(len(gas)):
            total_gas += gas[i]     # Total gas available
            total_cost += cost[i]   # Total cost to travel
            
            # Update current balance (gas remaining after traveling from station i)
            current_balance += gas[i] - cost[i]
            
            # If the current balance is negative, we can't start from the current start station
            if current_balance < 0:
                # Set the next station as the starting point
                start_station = i + 1
                # Reset current balance because we can't start from previous stations
                current_balance = 0
        
        # If total gas is less than total cost, it is impossible to complete the circuit
        if total_gas < total_cost:
            return -1
        else:
            return start_station

# Example usage
sol = Solution()
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
output = sol.canCompleteCircuit(gas, cost)
print(output)