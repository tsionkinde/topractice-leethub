import math
from collections import Counter
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count=Counter(s)
        for i in count:
            if i==letter:
                return math.floor((count[i]/len(s))*100)
        return 0        

        