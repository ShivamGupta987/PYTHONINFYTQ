# leetcodee problem non 1047 

def remove_dupli(input_str):
    set_str=set()
    stack=[]
    input_string = input_str 
    
    for i in input_string:
        if i not in set_str:
            set_str.add(i)
            stack.append(i)
    return "".join(stack)


input_str = "aabcc"
result = remove_dupli(input_str)
print(result)
            
            
# mwethod 2 

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack =[]

        for i in s:
            if len(stack) == 0:
                stack.append(i)
            elif i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
        

    
# leetcode valid parenthese problem no 20

class Solution:
    def isValid(self, s: str) -> bool:
        open_braces = ["[","{","("]
        closed_braces = ["]","}",")"]
        stack =[]

        for i in s:
            if i in open_braces:
                stack.append(i)

            elif i in closed_braces:
                if len(stack) == 0:
                    return  
                index = closed_braces.index(i)
                if open_braces[index] == stack[-1]:
                    stack.pop()
                else:
                    return False 

        return len(stack) == 0    
    
    # method 2
    
    def isValid(self, s: str) -> bool:
        stack = []
        open_braces = ["(", "{"]
        closed_braces = [")", "}"]
        
        for i in s:
            if i in open_braces:
                stack.append(i)
            elif i in closed_braces:
                if len(stack) == 0:
                    return False
                index = closed_braces.index(i)
                if open_braces[index] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0

# Example usage:
sol = Solution()
print(sol.isValid("{()}"))  # Output: True
print(sol.isValid("{[}"))   # Output: False


# rewriteeee

# leetcodee problem non 1047 

def remove_dupli(input_str):
    set_str=set()
    stack=[]
    input_string = input_str 
    
    for i in input_string:
        if i not in set_str:
            set_str.add(i)
            stack.append(i)
    return "".join(stack)


input_str = "aabcc"
result = remove_dupli(input_str)
print(result)
            
            
# mwethod 2 

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack =[]

        for i in s:
            if len(stack) == 0:
                stack.append(i)
            elif i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
        

    
# leetcode valid parenthese problem no 20

class Solution:
    def isValid(self, s: str) -> bool:
        open_braces = ["[","{","("]
        closed_braces = ["]","}",")"]
        stack =[]

        for i in s:
            if i in open_braces:
                stack.append(i)

            elif i in closed_braces:
                if len(stack) == 0:
                    return  
                index = closed_braces.index(i)
                if open_braces[index] == stack[-1]:
                    stack.pop()
                else:
                    return False 

        return len(stack) == 0    
    
    # method 2
    
    def isValid(self, s: str) -> bool:
        stack = []
        open_braces = ["(", "{"]
        closed_braces = [")", "}"]
        
        for i in s:
            if i in open_braces:
                stack.append(i)
            elif i in closed_braces:
                if len(stack) == 0:
                    return False
                index = closed_braces.index(i)
                if open_braces[index] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0

sol = Solution()
print(sol.isValid("{()}"))  
print(sol.isValid("{[}"))  

# leetcode 503


from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n  
        stack = []  

        for i in range(2 * n):
            num = nums[i % n]  
            

            while stack and nums[stack[-1]] < num:
                index = stack.pop()  
                res[index] = num  
            
         
            stack.append(i % n)
        
        return res
    
# 1944 problems on stack leetcode

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n =len(heights)
        result = [0]*n
        stack = []

        for i in range(n-1,-1,-1):
            height = heights[i]
            visibility = 0
            while stack and height > stack[-1]:
                stack.pop()
                visibility+=1
            if(stack):
                visibility+=1

            result[i]=visibility
            stack.append(height)
        return result
        
#leetcode 155 problem solved min stack

class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]
        self.size=0
        

    def push(self, val: int) -> None:
        if self.size == 0:
            self.minStack.append(val)
        if val <= self.minStack[-1]:
            self.minStack.append(val)
        self.stack.append(val)
        self.size+=1
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()