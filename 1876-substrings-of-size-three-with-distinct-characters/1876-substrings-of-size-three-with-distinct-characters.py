class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count=0
        window=s[:3]
        if len(set(window))==3:
            count+=1
        for i in range(3,len(s)):
            window=window[1:]+s[i]
            if len(set(window))==3:
                count+=1
           
        return count        
        
        