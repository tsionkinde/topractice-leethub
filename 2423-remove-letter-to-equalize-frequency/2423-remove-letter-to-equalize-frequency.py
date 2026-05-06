from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            temp = word[:i] + word[i+1:]
            freq = Counter(temp)
            values = list(freq.values())
            
            if len(set(values)) == 1:
                return True
                
        return False