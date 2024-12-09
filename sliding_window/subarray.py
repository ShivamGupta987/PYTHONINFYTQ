def maximum_sum_subarray(arr,k):
    sum=0
    i=0
    while i<k:
        sum+=arr[i]
        i+=1
        
    ans = sum 
    while i<len(arr):
        sum-=arr[i-k]
        sum+=arr[i]
        ans=max(ans,sum)
        i+=1
    return ans


arr = [100,200,300,400,500]
print(maximum_sum_subarray(arr,3))