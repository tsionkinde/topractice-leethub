class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        first_letters=''
        for i in words:
            first_letters+=i[0]
        if first_letters==s:
            return True
        else:
            return False        
        