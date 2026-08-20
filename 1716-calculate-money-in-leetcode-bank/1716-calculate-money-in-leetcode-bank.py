class Solution:
    def totalMoney(self, n: int) -> int:
        total=0
        monday=1
        for i in range(n):
            total+=monday+(i%7)
            if (i+1)%7==0:
                monday+=1
                
        return total    

        