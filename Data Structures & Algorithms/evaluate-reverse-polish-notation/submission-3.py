class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for ch in tokens:
            if ch in ("+", "-", "*", "/"):
                right = s.pop()
                left = s.pop()
                
                if ch == '+': 
                    s.append(left + right)
                elif ch == '-':
                    s.append(left - right)
                elif ch == '*':
                    s.append(left * right)
                elif ch == '/':
                    s.append(int(left / right))
            else:
                s.append(int(ch))

        return s.pop()
