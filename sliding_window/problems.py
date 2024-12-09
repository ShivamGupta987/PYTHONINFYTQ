# 1052 grummpy leetcode



class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)

        # Step 1: Calculate initially satisfied customers outside grumpy periods
        satisfied_customer = 0
        for i in range(n):
            if grumpy[i] == 0:
                satisfied_customer += customers[i]

        # Step 2: Calculate additional customers satisfied in the initial 'minutes' window
        max_satisfied = 0
        additional_satisfied = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                additional_satisfied += customers[i]

        max_satisfied = additional_satisfied

        # Step 3: Sliding window to maximize the additional satisfied customers in any 'minutes' window
        for i in range(minutes, n):
            if grumpy[i] == 1:
                additional_satisfied += customers[i]
            if grumpy[i - minutes] == 1:
                additional_satisfied -= customers[i - minutes]

            # Update the max satisfied including always satisfied customers
            max_satisfied = max(max_satisfied, additional_satisfied)

        # Step 4: Return total satisfied customers, including both always and maximized additionally satisfied
        return satisfied_customer + max_satisfied


# 209 leetcode min array

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        ans = float("inf")
        total = 0

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                ans = min(ans,right-left+1)
                total -= nums[left]
                left+=1 

        return 0 if ans == float("inf") else ans



# 1493 leetcode  1and 0
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        zeros = 0
        ans = 0
        for right in range(n):
            if nums[right]==0:
                zeros+=1

            while zeros>1:
                if nums[left]==0:
                    zeros-=1
                left+=1


            ans = max(ans,right-left+1-zeros)
        return ans if ans!=n else ans-1
    
    # 1004 leetcode max ones
    
    class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0 
        ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k-=1
            if k < 0:
                if nums[left]==0:
                    k+=1
                left+=1
            ans = max(ans,right-left+1)

        return ans
    
    # 713 leetcode
    
    class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k ==0:
            return 0
        
        count = 0

        product =1

        i=0
        for j in range(len(nums)):
            product*=nums[j]
            while i<=j and product>=100:
                product/=nums[i]
                i+=1
            count+= j-i+1 


        return count


     