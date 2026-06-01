class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        addd=""
        for i in words:
            addd+=i
            if s==addd:
                return True
            if len(addd)>len(s):
                return False   
        else:
            return False        


            