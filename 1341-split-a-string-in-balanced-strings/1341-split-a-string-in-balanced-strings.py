class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance=0#it calculates no of R-no of L
        count=0#it represents the no of balanced string it increases when balance become zero because it is the point that no of R and no of L become equal
        for ch in s:
            if ch=='R':
                balance+=1
            else:
                balance-=1
            if balance==0:
                count+=1
        return count        


         

        