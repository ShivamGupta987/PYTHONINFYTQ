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
        