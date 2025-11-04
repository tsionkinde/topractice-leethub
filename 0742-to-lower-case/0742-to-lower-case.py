class Solution:
    def toLowerCase(self, s: str) -> str:
        #return s.lower() simply it convert to lower case
        result="" 
        for ch in s:
            if "A"<=ch <="Z":
                result+=chr(ord(ch)+32)
            else:
                result+=ch
        return  result           
