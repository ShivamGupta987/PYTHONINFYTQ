# leetcode 3.longest substring without repeating chr 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l=0
        res = 0 

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res,r-l+1)

        return res  
    
# leetcode 560 subarray sum equal K
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0 
        prefixSums = {0:1}

        for n in nums:
            curSum += n 
            diff = curSum - k 

            res +=  prefixSums.get(diff,0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum,0)
        return res