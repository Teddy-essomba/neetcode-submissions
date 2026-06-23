

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  # stores indices, temperatures decrease monotonically
        
        for i, temp in enumerate(temperatures):
            # While current temp is warmer than temp at top of stack
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index  # days until warmer
            stack.append(i)
        
        return res
            


        



        
        


    

        

        

        


        



        