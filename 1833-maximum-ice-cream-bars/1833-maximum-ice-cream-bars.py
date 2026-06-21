class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count=0
        costs.sort()
        for i in costs:
            if coins<i:
                break

            coins-=i
            count+=1
        return count    
            



        