from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res=[]
        s1=s1.split()
        s2=s2.split()
        count1=Counter(s1)
        count2=Counter(s2)
        for i in count1:
            if count1[i]==1 and count2[i]==0:
                res.append(i)
        for j in count2:
            if count2[j]==1 and count1[j]==0:
                res.append(j) 
        return res               

              
        