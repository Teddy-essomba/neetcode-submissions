class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        nums.sort()
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        pairs = sorted(count.items(), key=lambda item: item[1], reverse=True)

        res = []
        for key, value in pairs[:k]:
            res.append(key)
        return res






