class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0


        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length , longest)
        return longest


        
        

        # 0, 1, 2, 3, 4, 5, 6
        # 2, 3, 4, 5 , 10 , 20
        # -1 -1 0 1 3 4 5 6 7 8 9Failed Test Case
