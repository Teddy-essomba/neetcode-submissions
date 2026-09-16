import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
    
        for num, count in dic.items():
            heapq.heappush(heap, (count,num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(len(heap)):
            res.append(heap[i][1])

        return res
     



        
        
    

        


        
        















            

            

            
            




            

            


    
    
            

            
            



        