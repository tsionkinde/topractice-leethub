class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set=set()
        n=len(s)
        left=0
        res=0
        for right in range(n):
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1
            char_set.add(s[right])
            res=max(res,right-left+1)
        return res        
