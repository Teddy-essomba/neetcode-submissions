class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = nums.copy()

        for i in nums:
            res.append(i)
        
        return res
            
            

        

        