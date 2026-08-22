from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count=Counter(s)
        the_max=max(count.values())
        for value in count.values():
            if value!=the_max:
                return False
        return True        

        