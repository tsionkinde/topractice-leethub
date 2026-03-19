class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        exp=n
        if exp<0:
            x=1/x
            exp=-exp
        result=1
        while exp>0:
            if exp%2==1:
                result*=x
            x*=x
            exp//=2
        return result        


        