class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.empty():
            return self.stack.pop()
        return None

    def empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return str(self.stack)




class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = Stack()

        for token in tokens:
           
            if token.lstrip('-').isdigit():
                stack.push(int(token))
            else:
             
                num2 = stack.pop()
                num1 = stack.pop()
                
                # Perform the operation
                if token == '+':
                    result = num1 + num2
                elif token == '-':
                    result = num1 - num2
                elif token == '*':
                    result = num1 * num2
                elif token == '/':
                    # Integer division truncating toward zero
                    result = int(num1 / num2)
                
                stack.push(result)
        
        return stack.pop()
        
        
        


        