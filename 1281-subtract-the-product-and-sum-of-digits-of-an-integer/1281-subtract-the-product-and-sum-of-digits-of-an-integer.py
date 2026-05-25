class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x=str(n)
        prod=1
        addi=0
        for i in x:
            prod*=int(i)
            addi+=int(i)
        return prod-addi    

        