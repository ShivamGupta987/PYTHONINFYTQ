
# brute force approch
def negative(arr,k):
    n=len(arr)

    for i in range(0,n-k+1):
        flag = False
        for j in range(0,k):
            if arr[i+j]<0:
                print(arr[i+j])
                
                flag = True
                break 
        if not flag:
            print(0)
            
print(negative([0,-1,2,3,-4,5,-6,7],3))


#  2nd aprrocCH
FNI = 0
def negative(arr,k):

    for i in range(k-1,len(arr)):
        while (FNI<i) and (FNI <=i-k or arr[FNI]>=0):
            FNI+=1
            
        if FNI <=i and arr[FNI]<0:
            print(arr[FNI])
        else:
            print(0)