from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel=""
        conso=""
        for i in s:
            if i in "aeiou":
                vowel+=i
            else:
                conso+=i
        countV=Counter(vowel)
        countC=Counter(conso)
        x=max(countV.values(),default=0)
        y=max(countC.values(),default=0)
        return x+y
        
        
            

                     
      

        