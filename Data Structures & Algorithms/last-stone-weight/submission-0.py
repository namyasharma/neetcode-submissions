class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones)>=2:
                stones.sort()
                diff = stones[-1] - stones[-2]
                l = len(stones)
                stones = stones[0:l-1]
                stones[-1] = diff
                print(stones)  
        return stones[0] or 0        
            
              

        