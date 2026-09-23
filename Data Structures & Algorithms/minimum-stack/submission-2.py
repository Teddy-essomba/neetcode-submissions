class MinStack:

    def __init__(self):
        self.items = []
        self.min_stack = []
       

    def push(self, val: int) -> None:
        self.items.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        remove = self.items.pop()
        if remove == self.min_stack[-1]:
            self.min_stack.pop()

        

    def top(self) -> int:
        return self.items[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
