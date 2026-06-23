class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        R = 1
        L = 1
        n = len(nums)

        l_arr = [0] * n
        r_arr = [0] * n

        for i in range(n):
            j = -i -1

            l_arr[i] = L
            r_arr[j] = R

            L *= nums[i]
            R *= nums[j]

        return [l * r for l ,r in zip(l_arr, r_arr)]






       

            

            
        






        