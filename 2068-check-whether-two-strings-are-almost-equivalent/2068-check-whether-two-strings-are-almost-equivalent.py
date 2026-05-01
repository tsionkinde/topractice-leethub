from collections import Counter

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        
        count1=Counter(word1)
        count2=Counter(word2)
        for ch in set(count1.keys()).union(count2.keys()):           
            if abs(count1[ch]-count2[ch])>3:
                    return False
        return True            

             
            
        