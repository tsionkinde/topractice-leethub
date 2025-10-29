class Solution:
    def isPalindrome(self, x: int) -> bool:
        word=str(x)
        left=0
        right=len(word)-1
        while  left < right:
            if word[left]!=word[right]:
               
                return False
            right-=1
            left+=1    
                
        return True          

        