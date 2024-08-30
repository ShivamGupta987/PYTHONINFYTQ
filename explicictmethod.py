# class Calculator:
#     def add(self,a,b):
#         return a+b
#     def add(self,a,b,c):
#         return a+b+c
    
# cal = Calculator()

# print(cal.add(5,6,7))

# explicicit not working in python

# class Calculator:
#     def add(self,a,b):
#         return a+b
#     def add(self,a,b,c):
#         return a+b+c
    
# cal = Calculator()

# print(cal.add(5,6,7))
# print(cal.add(5,6))

# implicit working

# class Calculator:
   
#     def add(self,a,b,c=0):
#         return a+b+c
    
# cal = Calculator()

# print(cal.add(5,6,7))
# print(cal.add(5,6))



class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        # Create a copy of the original scores
        sorted_scores = sorted(score, reverse=True)
        # Prepare a list to store the result ranks
        ans = [""] * len(score)
        
        # Assign ranks based on the sorted scores
        for i in range(len(score)):
            # Find the position (rank) of the current score in the sorted list
            place = sorted_scores.index(score[i]) + 1
            
            # Assign the rank based on the position
            if place == 1:
                ans[i] = "Gold Medal"
            elif place == 2:
                ans[i] = "Silver Medal"
            elif place == 3:
                ans[i] = "Bronze Medal"
            else:
                ans[i] = str(place)  # 
            
        return ans


if __name__ == "__main__":
    solution = Solution()
    scores = [5, 8, 3, 2, 9]
    result = solution.findRelativeRanks(scores)
    print(result) 
                
    
        
    