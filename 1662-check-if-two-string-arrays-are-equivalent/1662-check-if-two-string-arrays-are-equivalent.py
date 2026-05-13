class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1=""
        for i in word1:
            w1+=i
        w2=""    
        for j in word2:
            w2+=j
        if w1==w2:
            return True
        else:
            return False            

       
        