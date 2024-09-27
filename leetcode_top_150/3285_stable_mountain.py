from typing import List

def stable_mountains(height: List[int], threshold: int) -> List[int]:
    result = []
    
    # Start from index 1, as index 0 is not considered stable
    for i in range(1, len(height)):
        # Check if the previous mountain is greater than the threshold
        if height[i - 1] > threshold:
            result.append(i)
    
    return result

# Example usage:
print(stable_mountains([1, 2, 3, 4, 5], 2))  # Output: [3, 4]
print(stable_mountains([10, 1, 10, 1, 10], 3))  # Output: [1, 3]
print(stable_mountains([10, 1, 10, 1, 10], 10))  # Output: []