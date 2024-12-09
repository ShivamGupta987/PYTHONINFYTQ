def negative(arr,k):
    n=len(arr)
    
    for i in range(0,n-k+1):
        for j in range(0,k):
            if arr[i+j]<0:
                print(arr[i+j])
                
                flag = True 
        if flag == False:
            print(0)
            
print(negative([0,-1,2,3,-4,5,-6,7],3))