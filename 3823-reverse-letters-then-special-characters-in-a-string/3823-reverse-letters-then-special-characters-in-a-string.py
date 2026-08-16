class Solution:
    def reverseByType(self, s: str) -> str:
        chars=""
        special=""
        res=""
        for i in s:
            if i.isalpha():
                chars+=i
            else:
                special+=i
        chars=chars[::-1]
        special=special[::-1] 
        char=0
        speci=0       
        for i in s:
            if i.isalpha():
                res+=chars[char]
                char+=1
            else:
                res+=special[speci]
                speci+=1                
        return res    


        