class Solution:
    def isPalindrome(self, x: int) -> bool:
       
    #    if string_num == string_num[::-1]:
    #        return True 
    #    else:
    #     return False  
        string_num = str(x) 
        
        l,r=0,len(string_num)-1
        while l<r:

            if string_num[l]!=string_num[r]:
                
                return False
            l+=1
            r-=1 
        return True  
        