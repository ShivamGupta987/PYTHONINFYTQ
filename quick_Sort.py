

# Method 1: Swapping for Partitioning
# In this method, we'll use a single pivot and swap elements to partition the array around this pivot.

def quicksort_swap(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quicksort_swap(left) + [pivot] + quicksort_swap(right)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort_swap(arr)
print(sorted_arr)


# Method 2: Left and Right Pointers for Partitioning
# In this method, we use left and right pointers to partition the array around a pivot element.