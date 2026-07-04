class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        before=""
        for i in range(k-1,-1,-1):
            before+=s[i]
        return before+s[k:]    

     
        