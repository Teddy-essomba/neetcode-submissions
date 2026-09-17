class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        sett = set(nums)


        for num in nums:
            if num - 1 not in sett:
                current_num = num
                current_streak = 1

                while current_num + 1 in sett:
                    current_num += 1
                    current_streak += 1
            
                longest = max(longest, current_streak)
        return longest




     
            
            



                

        




        
        