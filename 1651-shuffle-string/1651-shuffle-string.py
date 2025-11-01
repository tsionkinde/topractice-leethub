class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [''] * len(s)
        i = 0
        while i < len(s):
            result[indices[i]] = s[i]
            i += 1
        return ''.join(result)    



        