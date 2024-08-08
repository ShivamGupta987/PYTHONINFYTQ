# def max_sum_subarray(arr,k):
#     l=0
#     r=k-1
    
#     n =len(arr)
    
#     if k>n or k<=0:
#         print('error')
    
    
#     current_sum = sum(arr[:k])
#     max_sum = current_sum
    
#     while(r < n-1):
#         r+=1
#         current_sum+=arr[r]-arr[l]
#         l+=1
        
#         max_sum = max(max_sum,current_sum)
        
#     return max_sum

# arr= [-1,2,3,3,4,5,-1]
# k =4 
# print(max_sum_subarray(arr,k))


# def longest_subarray_with_sum(arr, k):
#     n = len(arr)
#     l, r = 0, 0
#     current_sum = 0
#     max_len = 0
    
#     while r < n:

#         current_sum += arr[r]
   
#         while current_sum > k:
#             current_sum -= arr[l]
#             l += 1
        

#         if current_sum <= k:
#             max_len = max(max_len, r - l + 1)
        

#         r += 1
    
#     return max_len


# arr = [2, 5, 1, 10, 10]
# k = 14
# print(longest_subarray_with_sum(arr, k))  



def longest_subarray(arr,k):
    l=0
    r=0
    c_s = 0 
    m_l = 0 
    n = len(arr)
    
    while(r<n):
        
        c_s = c_s+arr[r]
        
        while(c_s > k) :
            c_s = c_s - arr[l]
            l+=1 
        if c_s <=k :
            m_l = max(m_l,r-l+1)
        
        r+=1
    return m_l



arr = [2, 5, 1, 10, 10]
k = 14
print(longest_subarray(arr, k))  
