class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i in range(len(nums) - 1):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                triplet = [nums[i],nums[l],nums[r]]
                total = sum(triplet)
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    if triplet not in res:
                        res.append(triplet)
                    l += 1
        return res
            
            


            
            
        
'''
[-4,-1,-1,0,1,2]
    i     l r
  


'''