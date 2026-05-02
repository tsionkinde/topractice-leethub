class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)
        a=s[:n//2]
        b=s[n//2:]
        countA=0
        for i in a:
            if i in "aeiouAEIOU":
                countA+=1
        countB=0        
        for j in b:
            if j in "aeiouAEIOU":
                countB+=1
        if  countA ==  countB:
            return True
        else:
            return False    






        