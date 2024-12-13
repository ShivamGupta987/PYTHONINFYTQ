def max_sum(arr,k):
    l = 0
    r=k-1
    
    max_sum1 = 0
    n=len(arr)
   
    current_sum = 0
    current_sum = sum(arr[:k])
    while(r<n-1):
        r+=1
        current_sum=current_sum+arr[r]-arr[l]
        l+=1
        max_sum1 = max(current_sum,max_sum1)
        
    return max_sum1
arr = [1,5,4,2,9,9,9]
k = 3
print(max_sum(arr,k))

