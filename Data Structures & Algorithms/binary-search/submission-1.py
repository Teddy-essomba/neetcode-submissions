class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid  # Return the index when target is found
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1  # Return -1 if target is not found
            
            