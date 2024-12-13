

# def bubble_sort(Arr):
#     n = len(Arr)
    
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if Arr[j] > Arr[j+1]:
#                 Arr[j] , Arr[j+1]= Arr[j+1] , Arr[j]
                
#     return Arr
                
# Arr = [1,5,6,2,3]
# sorted_Arr = bubble_sort(Arr)
# print(sorted_Arr)




# def bubble_sort_enhanced(Arr):
#     n = len(Arr)
    
#     for i in range(n-1):
#         is_sorted = True
#         for j in range(n-i-1):
#             is_sorted = False
#             if Arr[j] > Arr[j+1]:
#                 Arr[j] , Arr[j+1]= Arr[j+1] , Arr[j]
                
#             if is_sorted == True :
#                 break
                
#     return Arr
                
# Arr = [1,5,6,2,3]
# sorted_Arr = bubble_sort_enhanced(Arr)
# print(sorted_Arr)


# def question(str,x):
    
#     my_list = str.split()
#     n = len(my_list)
    
#     for i in range(n-1,0,-2):
#         if int(my_list[i]) < x :
#             del[my_list[i-1:i+1]] 
            
#     n = len(my_list)
    
#     for i in range(1,n,2):
#         for j in range(1,n-i,2):
#             if int(my_list[j]) > int(my_list[j+2]) or (my_list[j-1]<my_list[j+1] and my_list[j] == my_list[j+1]):
#                 my_list[j],my_list[j+2] = my_list[j+2],my_list
#                 my_list[j-1], my_list[j+1] = my_list[j+1], my_list[j-1]
                
#     return " ".join(my_list)


# str = "Akshay 43 Shivam 92 hey 96 ghhuuhs 98"


# print(question(str,50))
# #  push all zeroes to the end
# def move_zeroes_to_end(arr):
#     # Initialize pointer to track the position of next non-zero element
#     non_zero = 0
    
#     # Iterate through the array
#     for current in range(len(arr)):
#         # If current element is non-zero, swap it with arr[non_zero]
#         if arr[current] != 0:
#             arr[non_zero], arr[current] = arr[current] ,arr[non_zero]
#             non_zero += 1
    
#     # Fill the rest of the array with zeroes from non_zero index to end
#     for i in range(non_zero, len(arr)):
#         arr[i] = 0
    
#     return arr

# # Example usage:
# arr = [0, 1, 0, 3, 12]
# result = move_zeroes_to_end(arr)
# print(result)  # Output: [1, 3, 12, 0, 0]





def non_zero(arr):
        non_zero = 0
        
        for i in range(len(arr)):
            if arr[i]!=0:
                arr[non_zero], arr[i] = arr[i], arr[non_zero]
                non_zero+=1 
                
        for i in range(non_zero,len(arr)):
            arr[i]=0
        return arr 


arr = [0, 1, 0, 3, 12]
result = non_zero(arr)
print(result) 
