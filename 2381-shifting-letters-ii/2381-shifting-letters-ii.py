class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)
        
   
        for l, r, direction in shifts:
            val = 1 if direction == 1 else -1
            diff[l] += val
            diff[r + 1] -= val
        
       
        result = []
        curr = 0
        for i, ch in enumerate(s):
            curr += diff[i]
          
            new_char = (ord(ch) - ord('a') + curr) % 26
            result.append(chr(ord('a') + new_char))
        
        return "".join(result)
        