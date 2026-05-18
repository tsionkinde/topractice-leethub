class Solution:
    def sumBase(self, n: int, k: int) -> int:
        def to_base_k(n, k):
            if n == 0:
                return "0"
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            res = ""
            while n > 0:
                res = digits[n % k] + res
                n //= k
            return res    
        res=to_base_k(n, k)        
        x=[]    
        for i in res:
            x.append(int(i))
        return sum(x)    
                

                