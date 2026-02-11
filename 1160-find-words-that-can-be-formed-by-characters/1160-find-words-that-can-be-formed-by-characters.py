
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
       
        res=0
        for w in words:
            can_form=True
            for ch in w:
                if w.count(ch)>chars.count(ch):
                    can_form=False
                    break
            if can_form:
                res+=len(w)
        return res        



        
        