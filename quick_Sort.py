

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


# Method 2: Left and Right Pointers for 
# 2nd emthdod
# In this method, we use left and right pointers to partition the array around a pivot element.


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_lr(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort_lr(arr, low, pi - 1)
        quicksort_lr(arr, pi + 1, high)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
quicksort_lr(arr, 0, len(arr) - 1)
print(arr)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_lr(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort_lr(arr, low, pi - 1)
        quicksort_lr(arr, pi + 1, high)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
quicksort_lr(arr, 0, len(arr) - 1)
print(arr)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_lr(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort_lr(arr, low, pi - 1)
        quicksort_lr(arr, pi + 1, high)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
quicksort_lr(arr, 0, len(arr) - 1)
print(arr)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_lr(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort_lr(arr, low, pi - 1)
        quicksort_lr(arr, pi + 1, high)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
quicksort_lr(arr, 0, len(arr) - 1)
print(arr)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_lr(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort_lr(arr, low, pi - 1)
        quicksort_lr(arr, pi + 1, high)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
quicksort_lr(arr, 0, len(arr) - 1)
print(arr)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_lr(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort_lr(arr, low, pi - 1)
        quicksort_lr(arr, pi + 1, high)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
quicksort_lr(arr, 0, len(arr) - 1)
print(arr)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_lr(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort_lr(arr, low, pi - 1)
        quicksort_lr(arr, pi + 1, high)

# chagpt code

class Quicksort:
    def quicksort(self, arr):
        self.sort(arr, 0, len(arr) - 1)

    def sort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.sort(arr, low, pi - 1)
            self.sort(arr, pi + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

# Example usage:
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    sorter = Quicksort()
    sorter.quicksort(arr)
    print("Sorted array:", arr)
    
    
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    sorter = Quicksort()
    sorter.quicksort(arr)
    print("Sorted array:", arr)
    
    
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    sorter = Quicksort()
    sorter.quicksort(arr)
    print("Sorted array:", arr)
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    sorter = Quicksort()
    sorter.quicksort(arr)
    print("Sorted array:", arr)
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    sorter = Quicksort()
    sorter.quicksort(arr)
    print("Sorted array:", arr)
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    sorter = Quicksort()
    sorter.quicksort(arr)
    print("Sorted array:", arr)
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    sorter = Quicksort()
    sorter.quicksort(arr)
    print("Sorted array:", arr)
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    sorter = Quicksort()
    sorter.quicksort(arr)
    print("Sorted array:", arr)


