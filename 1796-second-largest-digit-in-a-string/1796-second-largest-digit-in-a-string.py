class Solution:
    def secondHighest(self, s: str) -> int:
        res=set()
        for i in s:
            if i.isdigit():
                res.add(int(i))
        res=sorted(res)
        if len(res)>=2:
            return res[-2]
        else:
            return -1    
        
                
        