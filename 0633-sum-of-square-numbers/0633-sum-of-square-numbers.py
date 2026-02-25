class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int((c**0.5))+1):# i goes from 0 to square root of c
            remained=c-i*i
            j=int(remained**0.5)
            if j*j==remained:
                return True
        return False        

        