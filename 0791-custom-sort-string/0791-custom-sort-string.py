from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:   
        res=""
        count=Counter(s)
        for char in order:
            if char in count:                
                res+=char*count[char]
                del count[char]

        for char in count:
            res+=char*count[char]
            
            

            
               

        
        return res  

                       


        