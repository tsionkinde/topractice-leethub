class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = set(string.ascii_letters)
        l=0
        r=len(s)-1
        s=list(s)
        while l<r:
            if s[l] not in letters:
                l+=1
            elif s[r] not in letters:
                r-=1
            else:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1        
        return ''.join(s)        