# solution = []
# for index in indices:
#     sum = 0
#     for i in range(index + 1):
#         sum += arr[i]
#     solution.append(sum)



def prefix_Sum(arr):
    n = len(arr)
    pre_sum = [0]*n 
    # first element (0 index)   
    pre_sum[0] = arr[0]
    for i in range(1,n):
        pre_sum[i] = pre_sum[i-1]+arr[i]
    
    
    return pre_sum

arr = [10,20,10,5,15]

print(prefix_Sum(arr))

# for index value 

def prefix_Sum(arr):
    n = len(arr)
    pre_sum = [0] * n
    
    pre_sum[0] = arr[0]
    for i in range(1, n):
        pre_sum[i] = pre_sum[i - 1] + arr[i]
    
    return pre_sum

arr = [10, 20, 10, 5, 15]
prefix_sums = prefix_Sum(arr)

indices = [0, 2, 4]
solution = []

for ind in indices:
    solution.append(prefix_sums[ind])

print("Prefix Sums:", prefix_sums)
print("Selected Prefix Sums:", solution)

# # Q2 check if array can be partitioned into two continuous arrays of equal sum

def partition(arr):
    
    total = sum(arr)
    
    
    if total%2 !=0:
        return False 
    current_sum  = 0
    for num in arr:
        current_sum+=num
        if current_sum == total//2:
            return True
        
    return False


print(partition([1,1,1,2,1]))
        