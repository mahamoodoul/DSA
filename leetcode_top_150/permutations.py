def permute(arr):
    # Helper function to generate permutations
    def backtrack(start, end):
        if start == end:
            # If we've reached the end, print the permutation
            print(arr[:])
            print("end....4")
        else:
            for i in range(start, end):
                print("start....2")
                # Swap the current element with the element at the start index
                arr[start], arr[i] = arr[i], arr[start]
                # Recursively permute the remaining elements
                backtrack(start + 1, end)
                # Backtrack (swap back to the original configuration)
                arr[start], arr[i] = arr[i], arr[start]
                print("start....3")
    print("start....1")
    backtrack(0, len(arr))

# Test with the input list
words = [1,2,3]
permute(words)