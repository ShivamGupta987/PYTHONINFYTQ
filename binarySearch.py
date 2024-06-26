


# def binary_seacrh(arr,target):
    
#     low = 0 
#     high = len(arr) - 1
    
#     while low <= high:
#         mid = ((low + high) //2 )
        
#         if arr[mid] == target:
#             return mid 

#         elif arr[mid] <= target:
#             low = mid + 1 
        
#         else :
#             high = mid - 1
            
#     return -1 

# arr = [1,2,4,5,6,9,12,18,19]

# print(binary_seacrh(arr,12))


# # lower bound problem solved leetcode

# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         low = 0 
#         high = len(nums) - 1 

#         while low <= high :
#             mid = ((low + high) // 2)

#             if nums[mid] == target:
#                 return mid 

#             elif nums[mid] <= target:
#                 low = mid + 1 
                
#             else :
#                  high = mid - 1
                 

#         return low
        
        
#         #  2nd approach of ame question 
        
# def binary_seacrh(arr,target):
    
#     low = 0 
#     high = len(arr) - 1
    
#     while low <= high:
#         mid = ((low + high) //2 )
     

#         if arr[mid] >= target:
#             ans = mid
#             high = mid - 1
            
        
#         else :
#             low = mid + 1
            
            
#     return ans  

# arr = [1,2,4,5,6,9,12,18,19]

# print(binary_seacrh(arr,3))

# #  peajk mountain using binary

# class Solution:
#     def peakIndexInMountainArray(self, arr: List[int]) -> int:
#         low = 0 
#         high = len(arr)-1 

#         while low < high:
#             mid = ((low+high)//2)

#             if arr[mid] > arr[mid+1]:
#                 high = mid 
             
#             else:
#                 low = mid + 1
#         return low
        
# # another appraoch 

# def peak(arr):
#     n =  len(arr)
    
#     low =0 
#     high =len(arr) -1 
#     while low <= high:
#         mid = low + ((high-low)//2)
        
#         if ((mid==0) or arr[mid-1] < arr[mid]) and ((mid == n-1) or arr[mid+1]<arr[mid]):
#             return mid 
#         elif mid > 0 and arr[mid-1] > arr[mid]:
#             high = mid - 1
#         else:
#             low = mid+1 
            
#     return -1
            
            
#  first and last popsitoon leetcode 34 
# using binary
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         def find_first(nums, target):
#             low = 0
#             high = len(nums) - 1
#             first = -1

#             while low <= high:
#                 mid = (low + high) // 2
#                 if nums[mid] < target:
#                     low = mid + 1
#                 elif nums[mid] > target:
#                     high = mid - 1
#                 else:
#                     first = mid
#                     high = mid - 1

#             return first

#         def find_last(nums, target):
#             low = 0
#             high = len(nums) - 1
#             last = -1

#             while low <= high:
#                 mid = (low + high) // 2
#                 if nums[mid] < target:
#                     low = mid + 1
#                 elif nums[mid] > target:
#                     high = mid - 1
#                 else:
#                     last = mid
#                     low = mid + 1

#             return last
        
#         first_pos = find_first(nums, target)
#         last_pos = find_last(nums, target)
        
#         return [first_pos, last_pos]
    
# # using linear search sma e

#         def find_first(nums, target):
#             for i in range(len(nums)):
#                 if nums[i] == target:
#                     return i
#             return -1
        
#         def find_last(nums, target):
#             for i in range(len(nums)-1, -1, -1):
#                 if nums[i] == target:
#                     return i
#             return -1
        
#         first_pos = find_first(nums, target)
#         last_pos = find_last(nums, target)
        
#         return [first_pos, last_pos]
