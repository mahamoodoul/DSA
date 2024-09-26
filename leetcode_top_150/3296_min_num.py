def can_reduce_in_time(workerTimes, mountainHeight, mid):
    total_reduced = 0
    
    for time in workerTimes:
        # Calculate how much a worker can reduce in `mid` seconds
        x = 1
        sum_time = 0
        while True:
            current = time * x
            if sum_time + current > mid:
                break
            sum_time += current
            x += 1
        
        total_reduced += x - 1
        
        if total_reduced >= mountainHeight:
            return True
    
    return total_reduced >= mountainHeight

def min_time_to_reduce_mountain(mountainHeight, workerTimes):
    left, right = 0, mountainHeight * max(workerTimes)
    
    while left < right:
        mid = (left + right) // 2
        
        if can_reduce_in_time(workerTimes, mountainHeight, mid):
            right = mid
        else:
            left = mid + 1
    
    return left

# Example usage:
print(min_time_to_reduce_mountain(4, [2, 1, 1]))  # Output: 3
print(min_time_to_reduce_mountain(10, [3, 2, 2, 4]))  # Output: 12
print(min_time_to_reduce_mountain(5, [1]))  # Output: 15
