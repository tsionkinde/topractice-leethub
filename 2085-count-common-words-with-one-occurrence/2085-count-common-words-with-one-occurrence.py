from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        res=0
        count1=Counter(words1)
        count2=Counter(words2)
        for i in count1:
            if count1[i]==1 and count2[i]==1:
                res+=1
          
        return res                