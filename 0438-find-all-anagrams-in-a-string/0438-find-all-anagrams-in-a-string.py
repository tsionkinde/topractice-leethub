from collections import Counter 
# from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        char_set=set()
        n=len(p)
        res=[]
        p_count=Counter(p)
       
        for right in range(len(s)-n+1):
            window=s[right:right+n]

            if Counter(window)==p_count:
                res.append(right)
        return res        

       
        