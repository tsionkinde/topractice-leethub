class Solution:
    def sortVowels(self, s: str) -> str:
        vowels="aeiouAEIOU"
        VOW=[]
        for i in s:
            if i in vowels:
                VOW.append(i)
        VOW.sort()
        j=0
        result=list(s)
        for i in range(len(s)):
            if s[i] in vowels:                
                result[i]=VOW[j]
                j+=1
        return "".join(result)        




        