class Solution:
    def reverseDegree(self, s: str) -> int:
        the_sum=0
        for i in range(len(s)):
            the_sum+=(i+1)*(26-(ord(s[i])-ord('a')))
        return the_sum    

        