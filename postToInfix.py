stack= []
operator = set(['+','-','*','/','^'])
expression = "ab+c*"

for char in (expression):
    if char not in operator:
        stack.append(char)
    else:
        op1=stack.pop()
        op2=stack.pop()
        stack.append(f"({op1} {char} {op2})")
print(stack.pop())

# infix to postfix

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    postfix = []

    for char in expression:
        if char.isalnum():  # Check if the character is an operand (i.e., alphanumeric)
            postfix.append(char)
        elif char in precedence:  # Check if the character is an operator
            while (stack and stack[-1] != '(' and
                   precedence[char] <= precedence.get(stack[-1], 0)):
                postfix.append(stack.pop())
            stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Remove the '(' from the stack

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)

# Example usage
infix_expression = "a+b*c"
postfix_expression = infix_to_postfix(infix_expression)
print("Postfix Expression:", postfix_expression)

