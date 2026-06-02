class Solution:
    def sortSentence(self, s: str) -> str:
        res=""
        words=s.split()
        words=sorted(words,key=lambda x: (int(x[-1])))
        for x in words:
            res+=x[:-1] + " "
        return res.strip()   


       
        

        