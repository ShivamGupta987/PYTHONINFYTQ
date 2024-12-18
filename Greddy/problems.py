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
# 881 leetcode boat problem 

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat_count = 0
        start = 0
        end = len(people)-1

        while start<=end:
            if people[start]+people[end]<=limit:
                start+=1
                end-=1
                boat_count+=1

            else:
                end-=1
                boat_count+=1
        return boat_count
        
        
# 56 leetcode merge intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x:x[0])
        merged = []

        for interval in intervals:
            if not merged or interval[0]>merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1],interval[1])

        return merged


# 452 minimum number of arrows leetcode

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key = lambda x:x[1])
        arrow_pos = points[0][1]
        arrow_count = 1
        for i in range(1,len(points)):
            if arrow_pos >= points[i][0]:
                continue
            arrow_count +=1
            arrow_pos = points[i][1] 
        return arrow_count
    