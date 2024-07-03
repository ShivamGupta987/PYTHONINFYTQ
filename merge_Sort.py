def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively apply merge_sort to each half
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    
    # Merge the two halves into a sorted array
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    # Append any remaining elements
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    
    return result

# Example usage:
if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)
    
    # 2nd approach
    
def merge(arr,left_half,right_half):
    i=j=k =0
    
    while i<len(left_half) and j<len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i+=1
        else:
            arr[k]=right_half[j]
            j+=1
        k+=1
        
    #check any remain element
    
    while i<len(left_half):
        arr[k] = left_half[i]
        i+=1
        k+=1 
    while j<len(left_half):
        arr[k] = left_half[j]
        j+=1
        k+=1 
