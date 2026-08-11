class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        the_max=0
        for i in sentences:
            word=i.split()
            if len(word)>the_max:
                the_max=len(word)
        return the_max        
        