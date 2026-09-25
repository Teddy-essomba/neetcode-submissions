class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = [] 
        
        for i, current_temp in enumerate(temperatures):
            # Check if current temperature is warmer than the temperature at the top stack index
            while stack and current_temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                # The number of days is the difference between indices
                result[prev_index] = i - prev_index
            
            # Push the current day's index onto the stack
            stack.append(i)
            
        return result
