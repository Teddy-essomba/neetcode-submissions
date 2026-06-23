class Solution:
    def maxArea(self, heights: List[int]) -> int:

        L  = 0
        R = len(heights) - 1
        max_area = 0

        while L < R:
            height = min(heights[L], heights[R])  
            width = R - L
            area = height * width
            max_area = max(area, max_area)

            if heights[L] > heights[R]:
                R -= 1
            else:
                L += 1
        return max_area


        

