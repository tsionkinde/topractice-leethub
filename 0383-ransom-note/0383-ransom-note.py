from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran_count=Counter(ransomNote)
        mag_count=Counter(magazine)
        for char in ran_count:
            if ran_count[char]>mag_count[char]:
                return False
        return True        
          
        