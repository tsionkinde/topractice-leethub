class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        newWord=""
      
        for i in range(len(word)):
            if word[i]==ch:
                newWord += word[:i+1][::-1]+word[i+1:]
                return newWord
        return word        
                
                          

        