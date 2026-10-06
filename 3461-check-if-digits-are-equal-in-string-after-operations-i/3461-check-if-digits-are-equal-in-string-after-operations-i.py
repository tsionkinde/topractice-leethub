class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        while len(s)>2: 
            new=[]                      
            for i in range(1,len(s)):
                value=(int(s[i-1])+int(s[i]))%10
                new.append(str(value))
            s="".join(new)        
        if s[0]==s[1]:
            return True
        else:
            return False    




        