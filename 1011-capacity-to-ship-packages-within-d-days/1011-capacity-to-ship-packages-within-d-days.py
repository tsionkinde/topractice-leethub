class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            days_used=1
            current=0
            for w in weights:
                if w + current > capacity:
                    days_used+=1
                    current=0
                current+=w
            return days_used<=days
        left=max(weights)  
        right=sum(weights)
        while left<right:
            mid=(left+right)//2
            if canShip(mid):
                right=mid
            else:
                left=mid+1    
        return left        


        