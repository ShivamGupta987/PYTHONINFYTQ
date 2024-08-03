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
