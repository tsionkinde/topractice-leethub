class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev_n=""
        s_n=str(n)
        for i in range(len(s_n)-1,-1,-1):
            rev_n+=s_n[i]
        return abs(int(rev_n)-int(s_n))    
        