class Solution:
    def thousandSeparator(self, n: int) -> str:
        w = str(n)
        res = ""
        
        count = 0
        for i in range(len(w) - 1, -1, -1):
            res = w[i] + res
            count += 1
            
            if count == 3 and i != 0:
                res = "." + res
                count = 0
        
        return res