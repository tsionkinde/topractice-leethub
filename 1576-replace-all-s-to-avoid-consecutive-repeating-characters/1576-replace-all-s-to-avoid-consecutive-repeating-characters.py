class Solution:
    def modifyString(self, s: str) -> str:
        word=list(s)
        for i in range(len(word)):
            if word[i]=="?":
                left=word[i-1] if i>0 else None
                right=word[i+1] if i<len(word)-1 else None
                for char in "abc":
                    if char!=left and char!=right:
                        word[i]=char
                        break
        return "".join(word)             

        