class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces=text.count(' ')
        words=text.split()
        if len(words)==1:
            return words[0]+' '*spaces
        between=spaces//(len(words)-1)  
        extra=spaces % (len(words)-1) 
        res=(' '*between).join(words)
        res+=' '*extra
        return res 
           


        