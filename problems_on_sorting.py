#missing number leetcode
#1 method
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        expected_sum = n*(n+1) // 2 
        actual_sum = sum(nums)

        return expected_sum - actual_sum
        
        
#methdo 2 cycle sort
# time complexity = O(n)

def cycle_Sort(nums):
    i = 0 
    n = len(nums)
    while i < n:
        correct_index = nums[i]
        if nums[i]!=nums[correct_index] and nums[i] < n:
            nums[i],nums[correct_index] = nums[correct_index],nums[i] 
        else:
            i+=1 
            
    for i in range(n):
        if nums[i]!=i:
            return i
    return n
            
# leetcode 287 missing dupicate number 
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sorted_arr = sorted(nums)

        for i in range(1,len(sorted_arr)):
            if sorted_arr[i-1]==sorted_arr[i]:
                return sorted_arr[i]
        
        
#  leetcode 448 numbers dsiappperarerd 

class Solution:

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        num_set = set(nums)
        all_nums = set(range(1,n+1))

        missing_no = all_nums - num_set 
        return list(missing_no)
    
    
#  leetcode setmismatch problen 645 

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        duplicate = -1 
        n = len(nums)

        expected_sum = n*(n+1) // 2

        for i in range(1,n):
            if nums[i] == nums[i-1]:
                duplicate = nums[i]
                break
        actual_sum = sum(nums) - duplicate 

        missing = expected_sum - actual_sum 

        return [duplicate,missing]
        
#  2 method to solve same prroblem 

def find_dup(nums):
    n = len(nums)
    
    sum_n = n*(n+1)//2 
    sum_n_squared = n+(n+1)+(2*n+1) // 6
    
    sum_nums = sum(nums)
    sum_nums_squared = sum(x*x for x in nums)
    
    diff1 = sum_n - sum_nums 
    diff2 = sum_n_squared - sum_nums_squared
    
    missing_plus_duplicated = diff2//diff1 
    
    missing = (diff1 + missing_plus_duplicated)//2
    duplicate = missing - diff 
    
    return [ duplicate,missingg
    