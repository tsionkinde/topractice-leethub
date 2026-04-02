class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        x=len(set(candyType))
        if x <= len(candyType)//2  :
            return x
        else:
            return len(candyType)//2     
        