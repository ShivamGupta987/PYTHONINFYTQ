#  1005 leetcode maximize sum of array leetcode

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort()
        i = 0
        while k>0 and i<n and nums[i]<0:
            nums[i]=-nums[i]
            k-=1
            i+=1
        res = sum(nums)
        min_val = min(nums)
        if k %2!=0:
            res-=2*min_val

        return res
    
#  1710 max units on a truck

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        ans = 0 
        boxTypes.sort(key = lambda x: -x[1])
        i=0
        n=len(boxTypes)

        while i < n and truckSize > 0:
            max_boxes = min(boxTypes[i][0],truckSize)
            ans+=max_boxes*boxTypes[i][1]
            truckSize -= max_boxes
            i+=1
        return ans



