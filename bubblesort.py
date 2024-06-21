

def bubble_sort(Arr):
    n = len(Arr)
    
    for i in range(n-1):
        for j in range(n-i-1):
            if Arr[j] > Arr[j+1]:
                Arr[j] , Arr[j+1]= Arr[j+1] , Arr[j]
                
    return Arr
                
Arr = [1,5,6,2,3]
sorted_Arr = bubble_sort(Arr)
print(sorted_Arr)




def bubble_sort_enhanced(Arr):
    n = len(Arr)
    
    for i in range(n-1):
        is_sorted = True
        for j in range(n-i-1):
            is_sorted = False
            if Arr[j] > Arr[j+1]:
                Arr[j] , Arr[j+1]= Arr[j+1] , Arr[j]
                
            if is_sorted == True :
                break
                
    return Arr
                
Arr = [1,5,6,2,3]
sorted_Arr = bubble_sort_enhanced(Arr)
print(sorted_Arr)
