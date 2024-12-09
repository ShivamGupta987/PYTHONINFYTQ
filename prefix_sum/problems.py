# 1402 dishes reducing

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        

        satisfaction.sort()

        res = 0
        total = 0

        for i in range(len(satisfaction)-1,-1,-1):
            if satisfaction[i]+total>0:
                total+=satisfaction[i]
                res+=total
            else:
                break

        return res 
    
# 2389 leetcode

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        nums.sort()

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        ans = []

        for query in queries:
            index = self.binary_search(nums, query)
            ans.append(index)

        return ans

    def binary_search(self,nums,target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid + 1  
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    
# leetocde 238 product of array

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        output=[1]*n
        total=1

        for i in range(n):
            output[i] = total
            total*=nums[i]
        
        total = 1
        
        for i in range(n-1,-1,-1):
            output[i]*=total
            total*=nums[i]

        return output

   

        