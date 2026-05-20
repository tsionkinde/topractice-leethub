class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets=[]
        for i in range(97, 123): 
            alphabets.append(chr(i))
        for i in alphabets:
            if i not in sentence:
                return False
        return True        
        