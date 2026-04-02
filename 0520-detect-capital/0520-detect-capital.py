class Solution:
    def detectCapitalUse(self, word: str) -> bool:
      
        if word==word.capitalize()  or word.islower() or word.isupper():
            return True
        else:
            return False      
