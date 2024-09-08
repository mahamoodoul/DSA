from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Modify nums1 in-place to be the merged sorted array.
        """
        # If nums1 has no elements (m == 0), replace it with nums2
        if m == 0:
            nums1[:n] = nums2
            return nums1
        # If nums2 is empty (n == 0), nums1 is already correct, no need to do anything
        if n == 0:
            return nums1
        # Merge nums2 into nums1 and sort
        nums1[m:] = nums2  # Replace the remaining part of nums1 with nums2
        nums1.sort()  # Sort the list in-place
        return nums1

# Example usage
nums1 = [1, 2, 3, 0, 0, 0]  # nums1 has extra space for nums2
m = 3
nums2 = [2, 5, 6]
n = 3

# nums1 = [1]
# m = 1
# nums2 = []
# n = 0


# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1


obj = Solution()
obj.merge(nums1, m, nums2, n)
print(nums1)  # Output will be the sorted merged list


