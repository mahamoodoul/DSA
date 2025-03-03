from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        if len(nums) < 3:
            raise ValueError("Product requires at least three numbers")
        self.nums = nums


    def highestProductSort(self) -> int:
        """
        Calculate the highest product of three numbers using sorting.
        """
        nums.sort()
        # Return the maximum product
        return max(self.nums[-1] * self.nums[-2] * self.nums[-3], self.nums[0] * self.nums[1] * self.nums[-1])
    
    def highestProductWithoutSort(self) -> int:
        """
        Calculate the highest product of three numbers without sorting.
        """
       
        # Initialize the three largest and two smallest values
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')

        for num in self.nums:
            # Update the three largest values
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num

            # Update the two smallest values
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num

        # Calculate the two possible highest products
        product_with_max = max1 * max2 * max3
        product_with_min = min1 * min2 * max1

        # Return the maximum product
        return max(product_with_max, product_with_min)
        



# Example usage
nums = [1, 10, 2, 6, 5, 3]
output = Solution(nums)
print("with sorting: ",output.highestProductSort())
print("without sorting: ",output.highestProductWithoutSort())
