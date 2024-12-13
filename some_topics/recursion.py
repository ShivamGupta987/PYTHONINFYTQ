# def fctorial(n):
#     # base cond 
#     if n == 0:
#         return 1
#     else:
#         return n * fctorial(n-1)
# print(fctorial(5))
# def fibo(n):
#     # base cond 
#     if n<=1:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
# print(fibo(5))

#  print 1 to n using rucursion

# def print_no(n):
#     #base cond n>0
#     if n>0:
#         print_no(n-1)
#         print(n)
# print_no(5)
 
# print('--------------------------->>>>>>>>>>>>>>>') 

# #  print n to 1 using rucursion

# def print_no(n):
#     #base cond n>0
#     if n>0:
#         print(n)
#         print_no(n-1)
        
# print_no(5)


# # climbing stairs problem

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 0:
#             return 1
#         elif n < 0:
#             return 0 
#         else:
#             return self.climbStairs(n-1) + self.climbStairs(n-2)
        
#         # binary using recusion
# def binary_serach(arr,left,right,target):
#     if left > right:
#         return -1 
    
#     mid = left  + ((right-left)//2)
    
#     if arr[mid] == target:
#         return mid 
    
#     elif arr[mid] > target:
#         return binary_serach(arr,left,mid-1,target)
#     else:
#         return binary_serach(arr,mid+1,right,target)
    
    
# sub set of string 

def generate_subset(s,current= "",index =0):
    if index == len(s):
        print(current)
        return 
    
    generate_subset(s,current + s[index],index+1)
    generate_subset(s,current +index+1)
    
ex = "abc"
generate_subset(ex)
    
def generate_subset(s,current= "",index =0):
    if index == len(s):
        print(current)
        return 
    
    generate_subset(s,current + s[index],index+1)
    generate_subset(s,current +index+1)
