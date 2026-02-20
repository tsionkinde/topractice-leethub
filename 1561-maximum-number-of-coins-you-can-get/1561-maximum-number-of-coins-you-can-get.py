class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        a=0
        me=0
        bob=0
        while piles:
            a+=piles.pop()           
            me+=piles.pop()            
            bob+=piles.pop(0)
            
        return me    
            

            

            




        