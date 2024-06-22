


def binary_seacrh(arr,target):
    
    low = 0 
    high = len(arr) - 1
    
    while low <= high:
        mid = ((low + high) //2 )
        
        if arr[mid] == target:
            return mid 

        elif arr[mid] <= target:
            low = mid + 1 
        
        else :
            high = mid - 1
            
    return -1 

arr = [1,2,4,5,6,9,12,18,19]

print(binary_seacrh(arr,12))


# lower bound problem solved leetcode

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0 
        high = len(nums) - 1 

        while low <= high :
            mid = ((low + high) // 2)

            if nums[mid] == target:
                return mid 

            elif nums[mid] <= target:
                low = mid + 1 
                
            else :
                 high = mid - 1
                 

        return low
        
        